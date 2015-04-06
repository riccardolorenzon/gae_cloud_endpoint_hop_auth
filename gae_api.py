import webapp2
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models.entity import Entity
from google.appengine.ext import ndb

class GaeRequest(messages.Message):
  id_value = messages.StringField(1)
  string_value = messages.StringField(2, required=True)

class GaeResponse(messages.Message):
  id_value = messages.StringField(1, required=True)
  string_value = messages.StringField(2)

@endpoints.api(name='readWriteApi',version='v1',
               description='simple endpoint class with a read and write component')
class GaeApi(remote.Service):
    @endpoints.method(GaeRequest,
                  GaeResponse,
                  name='read',
                  http_method='GET')
    def read_value(self, request):
        """
        read component
        :param request:
        :return:
        """
        try:
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
        write component
        :param request:
        :return:
        """
        try:
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