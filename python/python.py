import logging

import webapp2
from webapp2_extras import sessions

class Python(webapp2.RequestHandler):
  def get(self):
    self.response.write("""

<html>
<head>
<script src="js/jquery.min.js"></script>
</head>
<body>
<script>
$.ajax({
  url: "eval"
  }).done(function(data) {
    console.log(data);
  })
</script>
</body>
</html>

""")

class Eval(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    import sys
    old_stdout = sys.stdout

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
    except Exception as e:
      self.response.write(e) 
    finally:
      sys.stdout = old_stdout

    self.response.write(wo.content)
app = webapp2.WSGIApplication([('/python/eval', Eval),
                               ('/python/.*', Python)],
                              debug=True)
