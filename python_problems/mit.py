from Problem import *    

problems = {}

def test1(closure):
    def f(n):
      if (n == 0): return 1
      else: return n * f(n-1)
    for i in range(10):
      assert(closure['fact'](i) == f(i))
problems[1] = Problem(intro='Write a function fact(n) that calculates the factorial of n.',test=test1)

def test5(closure):
    is_prime = closure['is_prime']
    primes = [2,3,5,7,11,13,17,19,23,29]
    for p in range(2,30):
        if (p in primes):
            assert(is_prime(p))
        else:
            assert(not(is_prime(p)))
problems[5] = Problem(intro='Determine if a number is prime.',test=test5)


def test6(closure):
    nth_prime = closure['nth_prime']
    primes = [2,3,5,7,11,13,17,19,23,29]
    for (i,p) in enumerate(primes):
        assert(nth_prime(i) == p)
problems[6] = Problem(intro='Find the nth prime. The 0th prime is 2.',test=test6)

"""
def nth_prime(n):
  i = 2
  count = n
  while (count > 0):
    i += 1
    if is_prime(i):
      count -= 1
  return i
"""

def test7(closure):
    return True
problems[7] = Problem(intro="""Write a program that computes the sum of the logarithms of all the primes from 2 to some
number n, and print out the sum of the logs of the primes, the number n, and the ratio of these
two quantities. Test this for different values of n.""",test=test7)
