import os, logging

import webapp2

from google.appengine.api.urlfetch import fetch, GET, POST
from urllib import urlencode
from urlparse import parse_qs

POCKET_REQUEST_URL = "https://getpocket.com/v3/oauth/request"
if os.environ['SERVER_SOFTWARE'].find('Development') >= 0:
  BASE_URL = "localhost:8080"
else:
  BASE_URL = "xuanji.appspot.com"
REDIRECT_URL = BASE_URL + "/echo/"

class Pocket(webapp2.RequestHandler):
  def get(self):
  
    request_payload = {
      'consumer_key': "11903-6214395f06bd09aa4b07dd76",
      'redirect_uri': REDIRECT_URL,
      'state': "nyan cat"
    }
  
    logging.info("fetching %s ...", POCKET_REQUEST_URL)
    response = fetch(url = POCKET_REQUEST_URL, method=POST, payload = urlencode(request_payload))

    request_token = parse_qs(response.content)['code'][0]
    
    logging.info("done. returned status code: %s, content: %s, code: %s", response.status_code, response.content, request_token)
    
    self.redirect("https://getpocket.com/auth/authorize?request_token=%s&redirect_uri=%s" % (request_token, REDIRECT_URL ))
    
    #self.response.out.write("<html>hello world</html>")

app = webapp2.WSGIApplication([('/pocket/login', Pocket)],
                              debug=True)
