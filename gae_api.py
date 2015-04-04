import webapp2
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

class GaeRequest(messages.Message):
  id_value = messages.StringField(1, required=True)
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
        try:
            gae_response = GaeResponse()
            gae_response.id_value = 'resource id : ' + request.id_value
            gae_response.string_value = 'value retrieved in db'
            return gae_response
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Couldn''t handle a GET request ' + TypeError.__str__())

    @endpoints.method(GaeRequest,
                  GaeResponse,
                  name='write',
                  http_method='POST')
    def write_value(self, request):
        try:
            return 'handled a POST request'
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Couldn''t handle a POST request ' + TypeError.__str__())