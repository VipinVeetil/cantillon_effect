"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: Weights Opt
	Module description: compute network weights to maximize output, given input prices
	input price along with input weights determine input quantitities
	input quantities along with production function parameters determine output
	
"""

from __future__ import division
import economic_functions as ef
import parameters
import numpy as np
from scipy.optimize import minimize
import parameters

def F(weights,prices):
	non_labor_inputs = weights[1:] / prices[1:]
	CES_output = ef.CES(non_labor_inputs, parameters.CES_exponent)
	labor_input = weights[0] / prices[0]
	cobb_douglas_quantities = [labor_input, CES_output]
	value = ef.cobb_douglas(cobb_douglas_quantities, parameters.cobb_douglas_exponents)
	return -value

def optimize(seed_weights, prices):
	cons = ({'type':'eq','fun':lambda x: 1 - sum(x)})
	bnds = []
	for i in xrange(len(seed_weights)):
		bnds.append((0,1))
	opt =  minimize(F, np.array(seed_weights), args=(np.array(prices)), method = 'SLSQP', bounds = bnds, constraints = cons, options = {'maxiter': 100000000})

	assert opt.success, opt
	optimal_weights = opt.x
	for weight in optimal_weights:
		assert weight >= 0
	assert 0.999 < sum(optimal_weights) < 1.001, (optimal_weights, sum(optimal_weights))


	return optimal_weights






