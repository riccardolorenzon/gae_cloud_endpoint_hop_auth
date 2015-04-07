import webapp2
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models.entity import Entity
from google.appengine.ext import ndb

WEB_CLIENT_ID = '70641680892-nkjkmbqbd9cmilcrg9sg7pbc6a9gch1a.apps.googleusercontent.com'

class GaeRequest(messages.Message):
  id_value = messages.StringField(1)
  string_value = messages.StringField(2, required=True)

class GaeResponse(messages.Message):
  id_value = messages.StringField(1, required=True)
  string_value = messages.StringField(2)

@endpoints.api(name='readWriteApi',version='v1',
               allowed_client_ids=[WEB_CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID],
               description='simple endpoint class with a read and write component',
               scopes=[endpoints.EMAIL_SCOPE])
class GaeApi(remote.Service):
    @endpoints.method(GaeRequest,
                  GaeResponse,
                  name='read',
                  http_method='GET')
    def read_value(self, request):
        """
        Get the entity based on its string value(if multiple entities are found the first one is fetched).
        If the entity does not exist it creates a new one and returns its string value and id.
        :param request:
        :return:
        """
        try:
            current_user = endpoints.get_current_user()
            if current_user is None:
                raise endpoints.UnauthorizedException('User not authenticated.')
            gae_response = GaeResponse()
            # get the entity from the string
            if not request.string_value:
                entity = None
            else:
                entity_list = Entity.query(Entity.string_value == request.string_value).fetch(1)
                if len(entity_list) != 0:
                    entity = entity_list[0]
                else:
                    entity = None
            if entity == None:
                entity = Entity(string_value=request.string_value)
                entity.put()
            entity_urlsafe = entity.key.urlsafe()
            gae_response.id_value = '{0}'.format(entity_urlsafe)
            gae_response.string_value = '{0}'.format(entity.string_value)
            return gae_response
        except Exception as ex:
            raise endpoints.NotFoundException('Couldn''t handle a GET request, ex:' + ex.message)

    @endpoints.method(GaeRequest,
                  GaeResponse,
                  name='write',
                  http_method='POST')
    def write_value(self, request):
        """
        Get the first entity with the provided string value, if the entity already exists in the datastore
        (if multiple entities are found the first one is fetched), returns the string value and the entity's id.
        Raise exception if entity does not exist.
        :param request:
        :return:
        """
        try:
            current_user = endpoints.get_current_user()
            if current_user is None:
                raise endpoints.UnauthorizedException('User not authenticated.')
            gae_response = GaeResponse()
            # get the entity from the string
            if not request.string_value:
                entity = None
            else:
                entity_list = Entity.query(Entity.string_value == request.string_value).fetch(1)
                if len(entity_list) != 0:
                    entity = entity_list[0]
                else:
                    entity = None
            if entity == None:
                raise endpoints.BadRequestException('Resource with string value {0} not found'.format(request.string_value))
            entity_urlsafe = entity.key.urlsafe()
            gae_response.id_value = '{0}'.format(entity_urlsafe)
            gae_response.string_value = '{0}'.format(entity.string_value)
            return gae_response
        except Exception as ex:
            raise endpoints.NotFoundException('Couldn''t handle a POST request, ex:' + ex.message)