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


"""
class WeightsOptimization(object):
	def __init__(self):
		self.CES_exponent = parameters.CES_exponent
		self.cobb_douglas_exponents = parameters.cobb_douglas_exponents
		self.method = parameters.weights_optimization_method

	def transform(self, x):
		y = x ** 2 / (1 + x **2)
		z = 1-sum(y), y
		return z

	def F(self, weights, input_prices):
		weights_tranformed = self.transform(weights)
		non_labor_inputs = weights_tranformed[1] / input_prices[1]	
		CES_output = ef.CES(non_labor_inputs, self.CES_exponent)
		labor_input = weights_tranformed[0] / input_prices[0]
		cobb_douglas_quantities = [labor_input, CES_output]
		value  = ef.cobb_douglas(cobb_douglas_quantities, self.cobb_douglas_exponents)
		return -value
	
	def optimize(self, seed_weights, prices):
		opt = minimize(self.F,np.array(seed_weights), args=(np.array(prices),), method =  self.method)
		optimal_weights = self.transform(opt.x)
		assert optimal_weights[0] >= 0.000
		for weight in optimal_weights[1]:
			assert weight >= 0.000
		return optimal_weights
"""








