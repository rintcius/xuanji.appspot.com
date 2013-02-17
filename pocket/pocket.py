import os, logging

import webapp2
from webapp2_extras import sessions

from google.appengine.api.urlfetch import fetch, GET, POST
from urllib import urlencode
from urlparse import parse_qs

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

POCKET_REQUEST_URL = "https://getpocket.com/v3/oauth/request"
if os.environ['SERVER_SOFTWARE'].find('Development') >= 0:
  BASE_URL = "localhost:8080"
else:
  BASE_URL = "xuanji.appspot.com"
REDIRECT_URL = BASE_URL + "/echo/"
    
class RequestTokenHandler(BaseHandler):
  def get(self):
  
    request_payload = {
      'consumer_key': "11903-6214395f06bd09aa4b07dd76",
      'redirect_uri': REDIRECT_URL
    }
  
    logging.info("fetching %s ...", POCKET_REQUEST_URL)
    response = fetch(url = POCKET_REQUEST_URL, method=POST, payload = urlencode(request_payload))

    request_token = parse_qs(response.content)['code'][0]
    
    logging.info("done. returned status code: %s, content: %s, code: %s", response.status_code, response.content, request_token)
    self.session['request_token'] = request_token
        
    self.redirect("https://getpocket.com/auth/authorize?request_token=%s&redirect_uri=%s" % (request_token, REDIRECT_URL ))
    
class AccessTokenHandler(BaseHandler):
  pass
    

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'some-secret-key',
}

app = webapp2.WSGIApplication([('/pocket/request',  RequestTokenHandler)],
                              debug=True, config=config)
