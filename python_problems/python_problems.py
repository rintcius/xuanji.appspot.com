from Problem import *    

problems = {}

def test1(closure):
    def f(n):
      if (n == 0): return 1
      else: return n * f(n-1)
    for i in range(10):
      assert(closure['fact'](i) == f(i))
problems[1] = Problem(intro='Write a function fact(n) that calculates the factorial of n.',test=test1)

def test3(closure):
    last = closure['last']
    assert(last([1,2,3]) == 3)
problems[3] = Problem(intro='Find the last element of a list.',test=test3)

def test4(closure):
    palindrome = closure['palindrome']
    assert(palindrome(['a','b','a']))
problems[4] = Problem(intro='Find out whether a list is a palindrome. A palindrome can be read forward or backward; e.g. [x,a,m,a,x].',test=test4)
