import cgi
import os

from google.appengine.api import users
from google.appengine.ext import webapp
import python_problems

from google.appengine.ext.webapp import template

form = """
              <form action="/python/%s" method="post">
                <div><textarea name="exec" rows="10" cols="60">%s</textarea></div>
                <div><input type="submit" value="submit"></div>
              </form>
"""

class python(webapp.RequestHandler):


    def serve_home(self):
        
        template_values = {
            'problems':python_problems.problems
        }

        path = os.path.join(os.path.dirname(__file__), 'python.html')
        self.response.out.write(template.render(path, template_values))

    def get(self, problem_id):
        
        if (problem_id == ''):
            return self.serve_home()
                
        template_values = {
            'intro': python_problems.problems[int(problem_id)].intro,
            'id': problem_id,
            'code': ""
        }
        path = os.path.join(os.path.dirname(__file__), 'problem.html')
        self.response.out.write(template.render(path, template_values))
          
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
            closure = {}
            exec exec_stmt in closure
            python_problems.problems[int(problem_id)].test(closure)
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

