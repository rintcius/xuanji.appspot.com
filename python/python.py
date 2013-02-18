import logging

import webapp2
from webapp2_extras import sessions

class Python(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    import sys
    out = sys.stdout

    class WriteLog:
      def __init__(self):
        self.content = ""
    def write(self, string):
          self.content += string

    wo = WriteLog()

    try:
      sys.stdout = wo
      closure = {}
      exec exec_stmt in closure
      get_problems_in_pset(pset_name)[problem_id].test(closure)
    except AssertionError:
      passed = False 
    except:
      passed = "Error"
    finally:
      sys.stdout = out

    self.response.write('yo')

app = webapp2.WSGIApplication([('/python/.*', Python)],
                              debug=True)
