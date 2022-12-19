# version code d7da415c4b69+
# Please fill out this stencil and submit using the provided submission script.

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from mat import Mat
from vec import Vec

## 10: (Problem 4.17.13) Linear-combinations matrix-vector multiply
# You are also allowed to use the matutil module
def lin_comb_mat_vec_mult(M, v):
    '''
    Input:
      -M: a matrix
      -v: a vector
    Output: M*v
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{'A','B'}), {('a','A'):7, ('a','B'):1, ('b','A'):-5, ('b','B'):2})
    >>> v=Vec({'A','B'},{'A':4, 'B':2})
    >>> lin_comb_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{'A','B'}), {('a','A'):8, ('a','B'):2, ('b','A'):-2, ('b','B'):1})
    >>> v1=Vec({'A','B'},{'A':4,'B':3})
    >>> lin_comb_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    from matutil import mat2coldict
    cols = mat2coldict(M)
    scaledcols = {k:v[k] * cols[k] for k in v.D}

    return Vec(M.D[0], {k0: sum([scaledcols[col][k0] for col in scaledcols]) for k0 in M.D[0]})

## 11: (Problem 4.17.14) Linear-combinations vector-matrix multiply
def lin_comb_vec_mat_mult(v, M):
    '''
    Input:
      -v: a vector
      -M: a matrix
    Output: v*M
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of vector-matrix multiplication. 
    Examples:
      >>> M=Mat(({'a','b'},{'A','B'}), {('a','A'):7, ('a','B'):1, ('b','A'):-5, ('b','B'):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> lin_comb_vec_mat_mult(v,M) == Vec({'A', 'B'},{'A': 19, 'B': 0})
      True
      >>> M1=Mat(({'a','b'},{'A','B'}), {('a','A'):8, ('a','B'):2, ('b','A'):-2, ('b','B'):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> lin_comb_vec_mat_mult(v1,M1) == Vec({'A', 'B'},{'A': 26, 'B': 11})
      True
    '''
    assert(v.D == M.D[0])
    from matutil import mat2rowdict
    rows = mat2rowdict(M)
    scaledcols = {k:v[k] * rows[k] for k in v.D}

    return Vec(M.D[1], {k1: sum([scaledcols[row][k1] for row in scaledcols]) for k1 in M.D[1]})

## 12: (Problem 4.17.15) dot-product matrix-vector multiply
# You are also allowed to use the matutil module
def dot_product_mat_vec_mult(M, v):
    '''
    Return the matrix-vector product M*v.
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
    >>> v=Vec({0,1},{0:4, 1:2})
    >>> dot_product_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
    >>> v1=Vec({0,1},{0:4,1:3})
    >>> dot_product_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    from matutil import mat2rowdict
    rows = mat2rowdict(M)
    return Vec(M.D[0], {k0: rows[k0]*v for k0 in M.D[0]})
  
## 13: (Problem 4.17.16) Dot-product vector-matrix multiply
# You are also allowed to use the matutil module
def dot_product_vec_mat_mult(v, M):
    '''
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of vector-matrix multiplication. 
    Examples:
      >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> dot_product_vec_mat_mult(v,M) == Vec({0, 1},{0: 19, 1: 0})
      True
      >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> dot_product_vec_mat_mult(v1,M1) == Vec({0, 1},{0: 26, 1: 11})
      True
      '''
    assert(v.D == M.D[0])

    from matutil import mat2coldict
    cols = mat2coldict(M)
    return Vec(M.D[1], {k1: cols[k1]*v for k1 in M.D[1]})

## 14: (Problem 4.17.17) Matrix-vector matrix-matrix multiply
# You are allowed to use the matutil module
def Mv_mat_mat_mult(A, B):
    '''
    >>> A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
    >>> B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
    >>> Mv_mat_mat_mult(A,B) == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
    True
    '''
    assert A.D[1] == B.D[0]

    from matutil import mat2coldict, coldict2mat
    cols = mat2coldict(B)

    return coldict2mat({v: A*cols[v] for v in cols})


## 15: (Problem 4.17.18) Vector-matrix matrix-matrix multiply
def vM_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    '''
    >>> A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
    >>> B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
    >>> vM_mat_mat_mult(A,B) == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
    True
    '''
    assert A.D[1] == B.D[0]

    from matutil import mat2rowdict, rowdict2mat
    rows = mat2rowdict(A)

    return rowdict2mat({v: rows[v] * B for v in rows})

## 16: (Problem 4.17.19) Comparing countries using dot-product
import io
from matutil import rowdict2mat
from vecutil import list2vec

with io.open("./part4_The_Matrix/UN_voting_data.txt", mode="r", encoding="utf-8") as f:
  outDict = {}
  for line in f:
      line = line.split()
      outDict[line[0]] = list2vec([int(x) for x in line[1:]])
  UNMatrix = rowdict2mat(outDict)
  
  M = UNMatrix* UNMatrix.transpose() 

  outM = Mat(M.D, {(key1, key2):M[(key1, key2)] for key1, key2 in M.f if key1 != key2 and key1 > key2})
  print("A")

  # Provide a set consisting of two strings
  most_opposed_pair_of_countries = (min(outM.f, key=outM.f.get), outM[min(outM.f, key=outM.f.get)])

  # Provide a ten-element list of two-element sets of strings
  most_opposed_10_pairs_of_countries = sorted(outM.f.items(), key=lambda x: x[1])[:10]

  # Provide a set consisting of two strings
  most_agreeing_pair_of_countries = (max(outM.f, key=outM.f.get), outM[max(outM.f, key=outM.f.get)])



## 17: (Problem 4.17.20) Dictlist Helper
def dictlist_helper(dlist, k):
    '''
    Input: a list dlist of dictionaries which all have the same keys, and a key k
    Output: the list whose ith element is the value corresponding to the key k 
            in the ith dictionary of dlist
    Example:
    >>> dictlist_helper([{'apple':'Apfel','bread':'Brot'},{'apple':'manzana', 'bread':'pan'},{'apple':'pomme','bread':'pain'}], 'apple')
    ['Apfel', 'manzana', 'pomme']
    '''
    return [dict[k] for dict in dlist]

dictlist_helper([{'apple':'Apfel','bread':'Brot'},{'apple':'manzana', 'bread':'pan'},{'apple':'pomme','bread':'pain'}], 'apple')
# ['Apfel', 'manzana', 'pomme']

## 18: (Problem 4.17.21) Solving 2x2 linear systems and finding matrix inverse
solving_systems_x1 = ...
solving_systems_x2 = ...
solving_systems_y1 = ...
solving_systems_y2 = ...
solving_systems_m = Mat(({0, 1}, {0, 1}), {...:...})
solving_systems_a = Mat(({0, 1}, {0, 1}), {...:...})
solving_systems_a_times_m = Mat(({0, 1}, {0, 1}), {...:...})
solving_systems_m_times_a = Mat(({0, 1}, {0, 1}), {...:...})



## 19: (Problem 4.17.22) Matrix inverse criterion
# Please write your solutions as booleans (True or False)

are_inverses1 = ...
are_inverses2 = ...
are_inverses3 = ...
are_inverses4 = ...

