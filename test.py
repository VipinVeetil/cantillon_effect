
from __future__ import division
import numpy as np

import numba
from numba import jit
import economic_functions as ef
from scipy.optimize import minimize


def trans_x(x):
	x1 = x**2/(1+x**2)
	z  = np.hstack((x1, 1-sum(x1)))
	return z

def F(x, y, gamma = 0.2):
	z = trans_x(x)
	return -(((z/y)**gamma).sum())**(1./gamma)

y = [1,2,3]



opt = minimize(F, np.array([0.5, 0.2]), args=(np.array(y),), method='TNC')
a = trans_x(opt.x)
print a, sum(a), 'TNC'


opt = minimize(F, np.array([0.5, 0.2]), args=(np.array(y),), method='Nelder-Mead')
a = trans_x(opt.x)
print a, sum(a), 'Nelder-Mead'

def F_simple(x, y, gamma = 0.2):
	return -(((x/y)**gamma).sum())**(1./gamma)


cons = ({'type': 'eq', 'fun': lambda x: 1 - x[0] - x[1] - x[2]})
bnds = ((0, 1), (0, 1), (0, 1))
bnds = []
for i in xrange(3):
	bnds.append((0,1))

print bnds
opt = minimize(F_simple, np.array([0.5, 0.2, 0.3]), args=(np.array(y),), method='SLSQP', bounds = bnds, constraints = cons)
print opt.x, sum(opt.x), 'SLSQP'
