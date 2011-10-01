from Problem import *    

problems = {}

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

