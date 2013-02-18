import cgi
import os

import webapp2

from google.appengine.ext.webapp import template
from python_grading import python

class MainPage(webapp2.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, {}))

        
app = webapp2.WSGIApplication(
                             [('/', MainPage),
                              ('/python(.*)', python)],
                              debug=True)
