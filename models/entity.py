from google.appengine.ext import ndb

class Entity(ndb.Model):
  """
  Models a simple generic entity(only for test)
  """
  string_value = ndb.StringProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)
