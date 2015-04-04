import webapp2
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

class GaeRequest(messages.Message):
  string_value = messages.StringField(10)
  number_value = messages.IntegerField(2, required=True)

class GaeResponse(messages.Message):
  string_value = messages.StringField(10)

@endpoints.api(name='gaeApi',version='v1',
               description='simple endpoints with a read and write component')
class GaeApi(remote.Service):
    @endpoints.method(GaeRequest,
                  GaeResponse,
                  name='read',
                  http_method='GET')
    def read(self, request):
        try:
            gae_response = GaeResponse()
            gae_response.string_value = 'hi'
            return gae_response
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Couldn''t handle a GET request ' + TypeError.__str__())

    @endpoints.method(GaeRequest,
                  GaeResponse,
                  name='write',
                  http_method='POST')
    def write(self, request):
        try:
            return 'handled a POST request'
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Couldn''t handle a POST request ' + TypeError.__str__())