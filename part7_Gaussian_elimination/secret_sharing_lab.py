# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import random
from GF2 import one
from vecutil import list2vec
from part6_Dimension.independence import is_independent

## 1: (Task 7.7.1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    assert s == one or s == 0
    assert t == one or t == 0

    u = list2vec([randGF2() for i in range(6)])
    
    if a0*u == s and b0*u == t:
        return u
    else:
        return choose_secret_vector(s,t)

## 2: (Task 7.7.2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
import itertools
import sys
sys.setrecursionlimit(10000)

def generate_vectors ():
    vec = [a0,b0] + [list2vec([randGF2() for i in range(6)]) for i in range(8)]
    flag = True

    for group in list(itertools.permutations(vec, 3)):
        if is_independent(list(group)) == False:
            flag == False
            break

    if flag == False:
        return generate_vectors()
    else:
        return vec

[a0, b0, a1, b1, a2, b2, a3, b3, a4, b4] = generate_vectors()