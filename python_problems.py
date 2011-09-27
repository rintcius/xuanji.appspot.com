import cgi

class Problem:
    def __init__(self,intro,test):
        self.intro=intro
        self.test =test
    def __repr__(self):
        return "hello"
    def short_intro(self):
        return self.intro.split('\n')[0].replace('</a>','')
    

problems = {}

def test1(closure):
    def f(n):
      if (n == 0): return 1
      else: return n * f(n-1)
    for i in range(10):
      assert(closure['fact'](i) == f(i))
problems[1] = Problem(intro='Write a function fact(n) that calculates the factorial of n.',test=test1)

def test2(closure):
    laser=closure['laser']
    def laser2(b):
        l='>v<^';x={'/':'^<v>','\\':'v>^<',' ':l};r=p=0
        b=b.split('\n')
        b[0]=1
        for row in b[1:]:
            r+=1
            for g in l:
                c=row.find(g)
                if-1<c:p=c+1j*r;d=g
        while' '<d:z=l.find(d);p+=1j**z;c=b[int(p.imag)][int(p.real)];d=x.get(c,' '*4)[z]
        return '#'<c
    assert(laser(r"""
    ##########
    #   / \  #
    #        #
    #   \   x#
    # >   /  #
    ########## 
    """))
    assert(not(laser(r"""
    ##########
    #   v x  #
    # /      #
    #       /#
    #   \    #
    ##########
    """)))
    assert(not(laser(r"""
    #############
    #     #     #
    # >   #     #
    #     #     #
    #     #   x #
    #     #     #
    #############
    """)))
    assert(laser(r"""
    ##########
    #/\/\/\  #
    #\\//\\\ #
    #//\/\/\\#
    #\/\/\/x^#
    ##########
"""))

problems[2] = Problem(intro="""Simulate a laser when given a maze. 
From: <a href=http://stackoverflow.com/questions/1480023/code-golf-lasers> Code Golf: Lasers </a>
<br />
Sample testcase:
<pre>
assert(laser(r""\"##########
                 #   / \  #
                 #        #
                 #   \   x#
                 # >   /  #
                 ########## ""\") == True)
</pre>
""", test=test2)
"""
def laser(b):
    l='>v<^';x={'/':'^<v>','\\':'v>^<',' ':l};r=p=0
    b=b.split('\n')
    b[0]=1
    for row in b[1:]:
        r+=1
        for g in l:
            c=row.find(g)
            if-1<c:p=c+1j*r;d=g
    while' '<d:z=l.find(d);p+=1j**z;c=b[int(p.imag)][int(p.real)];d=x.get(c,' '*4)[z]
    return '#'<c
"""

def test3(closure):
    last = closure['last']
    assert(last([1,2,3]) == 3)
problems[3] = Problem(intro='Find the last element of a list.',test=test3)

def test4(closure):
    palindrome = closure['palindrome']
    assert(palindrome(['a','b','a']))
problems[4] = Problem(intro='Find out whether a list is a palindrome. A palindrome can be read forward or backward; e.g. [x,a,m,a,x].',test=test4)

