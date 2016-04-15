
from __future__ import division
import numpy as np

import numba
from numba import jit
import economic_functions as ef


"""
l = [1,2,3,0,0.9,19,-1]
a = np.array(l)
print l
print a
"""


l = [2,3,1]

m  = [0.2, 0.1, 0.9]

l_sorted = sorted(l)

print l
print l_sorted

l_index = []

for i in l:
	l_index.append(l_sorted.index(i))

print l_index