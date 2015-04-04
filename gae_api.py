import webapp2
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models.entity import Entity
from google.appengine.ext import ndb

class GaeRequest(messages.Message):
  id_value = messages.StringField(1, required=True)
  string_value = messages.StringField(2)

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
            entity_key = ndb.Key("Entity", request.id_value)
            entity = entity_key.get()
            if entity == None:
                entity = Entity(string_value=request.string_value)
                entity_key = entity.put()
            gae_response.id_value = '{0}'.format(entity_key)
            gae_response.string_value = '{0}'.format(entity.string_value)
            return gae_response
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Couldn''t handle a GET request ' + TypeError.__str__())

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
            entity_key = ndb.Key("Entity", request.id_value)
            entity = entity_key.get()
            if entity_key == None:
                raise endpoints.ServiceException('requested entity {0} not found'.format(request.id_value))
            entity.string_value = request.string_value
            entity.put()
            gae_response.id_value = '{0}'.format(entity_key)
            gae_response.string_value = '{0}'.format(entity.string_value)
            return gae_response
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Couldn''t handle a POST request ' + TypeError.__str__())