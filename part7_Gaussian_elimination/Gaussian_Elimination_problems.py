# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from matutil import *
from GF2 import one
from echelon import transformation

## 2: (Problem 7.9.3) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> is_echelon([[1,1]])
        True
        >>> is_echelon([[1]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
        >>> is_echelon([[2,1,0],[0,-4,0],[0,0,1]])
        True
        >>> is_echelon([[2,1,1],[-4,0,0],[0,0,1]])
        False
        >>> is_echelon([[2,1,1],[0,3,0],[1,0,1]])
        False
        >>> is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]])
        True
    '''

    firstNonzero = -1
    for row in A:
        newFirstNonZero = next((i for i, x in enumerate(row) if x), None)
        newFirstNonZero = newFirstNonZero if newFirstNonZero else 0

        if newFirstNonZero > firstNonzero:
            firstNonzero = newFirstNonZero
        else:
            return False
    return True

is_echelon([[1,1,1],[0,1,1],[0,0,1]])


## 4: (Problem 7.9.5) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = ...
solving_with_echelon_form_b = ...


from vecutil import zero_vec
## 5: (Problem 7.9.6) Echelon Solver
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True

    >>> b = [one, 0, one, one]
    >>> D = {'A', 'B', 'C', 'D','E'}
    >>> rowlist = [Vec(D, {'A': one, 'B':0, 'C':one, 'D':one, 'E':0}), Vec(D, {'A': 0, 'B':one, 'C':0, 'D':0, 'E':one}), Vec(D, {'A': 0, 'B':0, 'C':one, 'D':0, 'E':one}), Vec(D, {'A': 0, 'B':0, 'C':0, 'D':0, 'E':one})]
    >>> label_list = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(rowlist, label_list, b) == Vec({'B', 'C', 'A', 'D', 'E'},{'A':one, 'B': one, 'C':0, 'D':0, 'E':one})
    True

    >>> b = [one, 0, one, 0]
    >>> D = {'A', 'B', 'C', 'D','E'}
    >>> rowlist = [Vec(D, {'A': one, 'B':one, 'C':0, 'D':one, 'E':0}), Vec(D, {'A': 0, 'B':one, 'C':0, 'D':one, 'E':one}), Vec(D, {'A': 0, 'B':0, 'C':one, 'D':0, 'E':one}), Vec(D, {'A': 0, 'B':0, 'C':0, 'D':0, 'E':0})]
    >>> label_list = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(rowlist, label_list, b) == Vec({'B', 'C', 'A', 'D', 'E'},{'A':one, 'B': 0, 'C':one, 'D':0, 'E':0})
    True
    '''

    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]
        c = next((x for x in label_list if row[x]), None)
        if c:
            x[c] = (b[j] - x*row)/row[c]
        else:
            continue
    
    return x

b = [one, 0, one, 0]
D = {'A', 'B', 'C', 'D','E'}
rowlist = [Vec(D, {'A': one, 'B':one, 'C':0, 'D':one, 'E':0}), Vec(D, {'A': 0, 'B':one, 'C':0, 'D':one, 'E':one}), Vec(D, {'A': 0, 'B':0, 'C':one, 'D':0, 'E':one}), Vec(D, {'A': 0, 'B':0, 'C':0, 'D':0, 'E':0})]
label_list = ['A', 'B', 'C', 'D', 'E']
echelon_solve(rowlist, label_list, b) == Vec({'B', 'C', 'A', 'D', 'E'},{'A':one, 'B': 0, 'C':one, 'D':0, 'E':0})

## 6: (Problem 7.9.7) Solving General Matrices via Echelon

def solve(A, b):
    M = transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    row_list = [U_rows_dict[i] for i in sorted(U_rows_dict)]
    return echelon_solve(row_list,col_label_list, M*b)

def solve_var(A, b):
    M = transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    row_list = [U_rows_dict[i] for i in sorted(U_rows_dict)]
    return (row_list,col_label_list, M*b)

M = Mat(({'a', 'b', 'c', 'd'}, {'A', 'B', 'C', 'D'}), {
    ('a', 'A'): one, ('a', 'B'): one, ('a', 'D'): one,
    ('b', 'A'): one, ('b', 'D'): one,
    ('c', 'A'): one, ('c', 'B'): one, ('c', 'C'): one, ('c', 'D'): one,
    ('d', 'C'): one, ('d', 'D'): one
})
v = Vec(M.D[0], {'a': one, 'c': one})
(rowlist,col_label_list, mb) = solve_var(M, v)

rowlist = rowlist   # Provide as a list of Vec instances
label_list = col_label_list # Provide as a list
b = [mb[k] for k in sorted(mb.D)]          # Provide as a list of GF(2) values
