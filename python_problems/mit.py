from Problem import *    

problems = {}

def test_is_prime(closure):
    is_prime = closure['is_prime']
    primes = [2,3,5,7,11,13,17,19,23,29]
    for p in range(2,30):
        if (p in primes):
            assert(is_prime(p))
        else:
            assert(not(is_prime(p)))
problems[0] = Problem(intro="""Prime testing <br>
Determine if a number is prime.""",test=test_is_prime)

def test_nth_prime(closure):
    nth_prime = closure['nth_prime']

problems[1] = Problem(intro='Find the nth prime. The 0th prime is 2.',test=test_nth_prime)

def test_primorial(closure):
    primorial = closure['primorial']
    assert([primorial(i) for i in range(12)] == [1, 1, 2, 6, 6, 30, 30, 210, 210, 210, 210, 2310])
problems[2] = Problem(intro="""Primorial function n#


In this problem we investigate the properties of the primorial function n#, the product of all primes below n. Write such a function. You should have

0# = 1
1# = 1
2# = 2
3# = 6
4# = 6
5# = 30
6# = 30
7# = 120
8# = 210
9# = 210

Verify that n# < 4**n for n > 1. Prove it if you want.

""",test=test_primorial)

def test_log_primorial(closure):
    log_primorial = closure['log_primorial']
    [log_primorial(i) for i in range(2,50)]
    return True
    
problems[3] = Problem(intro="""More primorials

The tightest exponential bound on n# states that

n# ~ e**n

in the sense that the ratio approaches one. 

However, we cannot work directly with n# as it will be too large. Instead we can write it as

log n# ~ n

write something to calculate log n#.""",test=test_log_primorial)
