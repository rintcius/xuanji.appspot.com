import cgi
import os

from google.appengine.api import users
from google.appengine.ext import webapp
from python_problems import get_problems_in_pset

from google.appengine.ext.webapp import template

form = """
              <form action="/python/%s/%s" method="post">
                <div><textarea name="exec" rows="10" cols="60">%s</textarea></div>
                <div><input type="submit" value="submit"></div>
              </form>
"""

class python(webapp.RequestHandler):


    def serve_home(self, pset_name):
        
        template_values = {
            'pset_name':pset_name,
            'problems':get_problems_in_pset(pset_name)
        }

        path = os.path.join(os.path.dirname(__file__), 'python.html')
        self.response.out.write(template.render(path, template_values))

    def get(self, problem_id):
        
        parsed_id = problem_id.split('/')

        if problem_id == '':
            return #todo

        pset_name = parsed_id[0]
                
        if len(parsed_id) == 1:
            return self.serve_home(pset_name)
        
        problem_id = int(parsed_id[1])
        
        #now rendering a problem
        
        template_values = {
            'intro': get_problems_in_pset(pset_name)[problem_id].intro,
            'id': problem_id,
            'pset_name': pset_name,
            'code': ""
        }
        path = os.path.join(os.path.dirname(__file__), 'problem.html')
        self.response.out.write(template.render(path, template_values))
          
    def post(self, problem_id):
        
        parsed_id = problem_id.split('/')

        if len(parsed_id) != 2:
            print parsed_id
            return
        
        pset_name = parsed_id[0]
        problem_id = int(parsed_id[1])
        
        
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
            get_problems_in_pset(pset_name)[problem_id].test(closure)
        except AssertionError:
            passed = False 
        finally:
            sys.stdout = out


        if passed:
            self.response.out.write('<p style="color:green">passed all tests</p>')
        else:
            self.response.out.write('<p style="color:red">failed</p>')
                        
        self.response.out.write('</pre></body></html>')
        self.response.out.write(form % (pset_name, problem_id, exec_stmt))

