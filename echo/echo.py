import logging
import webapp2

from sessions import sessions
    
class Echo(sessions.BaseHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    
    out = """YOHeader

%s

Session

%s"""

    self.response.write(out % (self.request, self.session))

app = webapp2.WSGIApplication([('/echo/.*', Echo)],
                              debug=True, config=sessions.config)
