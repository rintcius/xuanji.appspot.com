import cgi
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from python_grading.python import python

from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

        
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/python(.*)', python)],
                                      debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
