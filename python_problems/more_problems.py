from Problem import *    

problems = {}

def test1(closure):
    def f(n):
      if (n == 0): return 1
      else: return n * f(n-1)
    for i in range(10):
      assert(closure['fact'](i) == f(i))
problems[1] = Problem(intro='Write a function fact(n) that calculates the factorial of n.',test=test1)
