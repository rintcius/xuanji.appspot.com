import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
import python_problems

form = """
              <form action="/python/%s" method="post">
                <div><textarea name="exec" rows="10" cols="60">%s</textarea></div>
                <div><input type="submit" value="submit"></div>
              </form>
"""

class python(webapp.RequestHandler):


    def get(self, problem_id):
        
        if (problem_id == ''):
            self.response.out.write('Hi. Go to python/1 or python/2')
            return
        self.response.out.write('<html><body>Problem: <br> <br>')
        self.response.out.write(python_problems.problems[int(problem_id)].intro)
        self.response.out.write('<p />')
        self.response.out.write(form%(problem_id,""))
        self.response.out.write('</html></body>')
          
    def post(self, problem_id):
        
        passed = True
        
        exec_stmt = self.request.get('exec')
        exec_stmt = exec_stmt.replace('\r\n', '\n')

        self.response.out.write('Output:<pre>')

        self.response.out.write(cgi.escape(exec_stmt + '\n'))
        
        self.response.out.write('<p style="color:blue">')
        
        import sys
        out = sys.stdout

        try:
            sys.stdout = self.response.out
            exec(exec_stmt+python_problems.problems[int(problem_id)].test,{})
        except AssertionError:
            passed = False 
        finally:
            sys.stdout = out


        if passed:
            self.response.out.write('<p style="color:green">passed all tests</p>')
        else:
            self.response.out.write('<p style="color:red">failed</p>')
                        
        self.response.out.write('</pre></body></html>')
        self.response.out.write(form % (problem_id, exec_stmt))

