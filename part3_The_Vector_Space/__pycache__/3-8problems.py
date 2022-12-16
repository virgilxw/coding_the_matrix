# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one

## 1: (Problem 3.8.1) Vector Comprehension and Sum

# Write and test a procedure vec select using a comprehension for the following computational
# problem:
# • input: a list veclist of vectors over the same domain, and an element k of the
# domain
# • output: the sublist of veclist consisting of the vectors v in veclist where v[k] is
# zero

def vec_select(veclist, k):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [v for v in veclist if v[k] == 0]


# Write and test a procedure vec sum using the built-in procedure sum(·) for the following:
# • input: a list veclist of vectors, and a set D that is the common domain of these
# vectors
# • output: the vector sum of the vectors in veclist.
# Your procedure must work even if veclist has length 0.
# Hint: Recall from the Python Lab that sum(·) optionally takes a second argument, which
# is the element to start the sum with. This can be a vector.
# Disclaimer: The Vec class is defined in such a way that, for a vector v, the expression 0 +
# v evaluates to v. This was done precisely so that sum([v1,v2,... vk]) will correctly
# evaluate to the sum of the vectors when the number of vectors is nonzero. However, this
# won’t work when the number of vectors is zero.

def vec_sum(veclist, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''

    return sum(veclist) if len(veclist) > 0 else 0

# Put your procedures together to obtain a procedure vec select sum for the following:
# • input: a set D, a list veclist of vectors with domain D, and an element k of the
# domain
# • output: the sum of all vectors v in veclist where v[k] is zero

def vec_select_sum(veclist, k, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return sum([v for v in veclist if v[k] == 0]) if len(veclist) > 0 else 0

## 2: (Problem 3.8.2) Vector Dictionary

# Write and test a procedure scale vecs(vecdict) for the following:
# • input: A dictionary vecdict mapping positive numbers to vectors (instances of Vec)
# • output: a list of vectors, one for each item in vecdict. If vecdict contains a key k
# mapping to a vector v, the output should contain the vector (1/k)v
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,4}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> result = scale_vecs({3: v1, 5: v2})
    >>> len(result)
    2
    >>> [v in [Vec({1,2,4},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})] for v in result]
    [True, True]
    '''

    return [vec/div for (div, vec) in vecdict.items()]

# Problem 3.8.3: Write a procedure GF2_span with the following spec:
# • input: a set D of labels and a list L of vectors over GF(2) with label-set D
# • output: the list of all linear combinations of the vectors in L
# (Hint: use a loop (or recursion) and a comprehension. Be sure to test your procedure on examples
# where L is an empty list.)

## 3: (Problem 3.8.3) Constructing a Span over GF(2)
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> result = GF2_span(D, [Vec(D, {'a': one, 'c': one}), Vec(D, {'c': one})])
    >>> len(result)
    4
    >>> [v in result for v in [Vec(D, {}),Vec(D, {'a': one, 'c': one}),Vec(D, {'c': one}),Vec(D, {'a':one})]]
    [True, True, True, True]
    '''

    outSet = set()
    def recur (X, prevVal):
        if X == []:
            outSet.add(prevVal)
        else:
            recur(X[1:], prevVal + one*X[0])
            recur(X[1:], prevVal + 0*X[0])

    recur(L, 0)
    
    return outSet

## 4: (Problem 3.8.7) Is it a vector space 1
# Answer with a boolean, please.
is_a_vector_space_1 = ...



## 5: (Problem 3.8.8) Is it a vector space 2
# Answer with a boolean, please.
is_a_vector_space_2 = ...



## 6: (Problem 3.8.9) Is it a vector space 3
# Answer with a boolean, please.
is_a_vector_space_3 = ...



## 7: (Problem 3.8.10) Is it a vector space 4
# Answer with a boolean, please.
is_a_vector_space_4a = ...
is_a_vector_space_4b = ...

