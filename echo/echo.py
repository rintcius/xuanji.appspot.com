import logging

import webapp2
from webapp2_extras import sessions

class BaseHandler(webapp2.RequestHandler):
  def dispatch(self):
    self.session_store = sessions.get_store(request=self.request)

    try:
      webapp2.RequestHandler.dispatch(self)
    finally:
      self.session_store.save_sessions(self.response)

  @webapp2.cached_property
  def session(self):
    return self.session_store.get_session()

class Echo(BaseHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    
    self.response.write("Header\n\n")
    self.response.write(self.request)
    self.response.write("\n\n\n")
    
    self.response.write("Session\n\n")
    self.response.write(self.session)

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'some-secret-key',
}

app = webapp2.WSGIApplication([('/echo/.*', Echo)],
                              debug=True, config=config)
