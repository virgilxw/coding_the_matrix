# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod
from factoring_support import intsqrt

import echelon

from math import ceil, sqrt

## 7.8.1
def root_method(N):
    '''
    Initialize integer a to be an integer greater than √N
• Check if √a2 - N is an integer.
• If so, let b = √a2 - N. Success! Return a - b.
• If not, repeat with the next greater value of a.
    '''

    def find_b(a, N):
        b = a**2-N

        if intsqrt(b)**2 == b:
            return a-sqrt(b)
        else:
            return find_b(a+1, N)

    a = ceil(sqrt(N))
    
    return find_b(a, N)

## 7.8.2
def gcd(x,y): return x if y == 0 else gcd(y, x % y)

from random import randint

r = randint(100000,999999)
s = randint(100000,999999)
t = randint(100000,999999)

a = r*s
b = s*t

d = gcd(a,b)

if a % d == 0 and b % d ==0 and d >=s:
    print("7.8.2 succeeded")
else:
    print("7.8.2 failed") 

## 7.8.3
# Let N = 367160330145890434494322103, let a = 67469780066325164, and
# let b = 9429601150488992, and verify that a ∗ a − b ∗ b is divisible by N. That means that
# the greatest common divisor of a − b and N has a chance of being a nontrivial divisor of
# N. Test this using the gcd procedure, and report the nontrivial divisor you found

N = 367160330145890434494322103
a = 67469780066325164
b = 9429601150488992

if (a*a - b*b)/N == True:
    print("axa-bxb is divisible")
else: 
    print("axa-bxb is not divisible") 

d = gcd(a-b, N)
if N/d % 1 == 0:
    print("divisor is " + str(d))

## 7.8.4
primeset={2, 3, 5, 7, 11, 13}
print("dumb_factor of 12 = ",  dumb_factor(12, primeset))
print("dumb_factor of 154 = ", dumb_factor(154, primeset))
print("dumb_factor of 2*3*3*3*11*11*13 = ", dumb_factor(2*3*3*3*11*11*13, primeset))
print("dumb_factor of 2*17 = ", dumb_factor(2*17, primeset))
print("dumb_factor of 2*3*5*7*19 = ", dumb_factor(2*3*5*7*19, primeset))


## Task 1, 7.8.5
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    if i % 2 == 1:
        return one
    else:
        return 0

## Task 2, 7.8.6
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, {k:int2GF2(i) for (k,i) in factors})

## Task 3, 7.8.7
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a tuple (roots, rowlist)
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    Example:
        >>> from factoring_support import primes
        >>> N = 2419
        >>> primeset = primes(32)
        >>> roots, rowlist = find_candidates(N, primeset)
        >>> set(roots) == set([51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79])
        True
        >>> D = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        >>> set(rowlist) == set([Vec(D,{2: one, 13: one, 7: one}),\
                Vec(D,{3: one, 19: one, 5: one}),\
                Vec(D,{2: one, 3: one, 5: one, 13: one}),\
                Vec(D,{3: one, 5: one, 7: one}),\
                Vec(D,{7: one, 2: one, 3: one, 31: one}),\
                Vec(D,{3: one, 19: one}),\
                Vec(D,{2: one, 31: one}),\
                Vec(D,{2: one, 5: one, 23: one}),\
                Vec(D,{5: one}),\
                Vec(D,{3: one, 2: one, 19: one, 23: one}),\
                Vec(D,{2: one, 3: one, 5: one, 13: one}),\
                Vec(D,{2: one, 3: one, 13: one})])
        True
    '''
    roots = []
    rowlist = []

    x = intsqrt(N)+2
    xo = x*x - N

    while len(roots) < len(primeset)+1:
        factored = dumb_factor(xo, primeset)
        if factored:
            roots.append(x)
            rowlist.append(make_Vec(primeset, factored))
            
        x = x+1
        xo = x*x - N

    return roots, rowlist

## 7.8.8

a = 53*77
b = 2 * 3 ** 2 * 5 * 13
gcd(a-b,N) == 1


# 7.8.9
a = 52 * 67 * 71
b = 2 * 3 ** 2 * 5 * 19 * 23
gcd(a-b,N)


## Task 4 7.8.10
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    Example:
        >>> roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
        >>> N = 2419
        >>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{1: one, 2: one, 11: one, 5: one})  
        >>> find_a_and_b(v, roots, N)
        (13498888, 778050)
        >>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one})
        >>> find_a_and_b(v, roots, N)
        (4081, 1170)
    '''

    alist = [roots[i] for i in range(len(roots)) if v[i] != 0]
    a = prod(alist)
    c = prod([x*x-N for x in alist])
    b = intsqrt(c)
    assert b*b == c
    return (a,b)

roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
N = 2419
v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{1: one, 2: one, 11: one, 5: one})  
find_a_and_b(v, roots, N)

## 7.8.11

def find_divisor (N, primeMax):
    primeset = set(list(primes(primeMax)))

    roots, rowlist = find_candidates(N, primeset)
    M = echelon.transformation_rows(rowlist)

    for i in list(range(-len(M), 0))[::-1]:
        
        v = M[i]
        a, b = find_a_and_b(v, roots, N)
        d = gcd(a-b,N)

        if d != 1:
            return d
        else:
            continue


## Task 5

nontrivial_divisor_of_2461799993978700679 = find_divisor(2461799993978700679, 10000)
print("nontrivial_divisor_of_2461799993978700679 = ", nontrivial_divisor_of_2461799993978700679)

## 7.8.12
nontrivial_divisor_of_20672783502493917028427 = find_divisor(20672783502493917028427, 10000)
print("nontrivial_divisor_of_20672783502493917028427 = ", nontrivial_divisor_of_20672783502493917028427) 