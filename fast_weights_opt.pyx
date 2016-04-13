"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Davoud Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Cython
	
	Module name: Weights Opt
	Module description: compute network weights to maximize output, given input prices
	input price along with input weights determine input quantitities
	input quantities along with production function parameters determine output
"""


from __future__ import division
import fast_economic_functions as ef
import parameters
cimport numpy as np
import numpy as np
from scipy.optimize import minimize
#from sys import float_epsilon

cdef double F(weights, double labor_price, non_labor_prices, double cobb_douglas_exponent_labor, double cobb_douglas_exponent_non_labor, double CES_exponent):
	cdef double value
	cdef double labor_input
	cdef double CES_output
	cdef np.ndarray non_labor_inputs
	cdef double labor_weight

	non_labor_inputs = weights[1:] / non_labor_prices
	CES_output = ef.CES(non_labor_inputs, CES_exponent)
	labor_input = weights[0] / labor_price
	value = labor_input ** cobb_douglas_exponent_labor * CES_output ** cobb_douglas_exponent_non_labor
	return -value

def optimize(seed_weights, prices):
	cdef double cobb_douglas_exponent_labor = parameters.cobb_douglas_exponent_labor
	cdef double cobb_douglas_exponent_non_labor = parameters.cobb_douglas_exponent_non_labor
	cdef double CES_exponent = parameters.CES_exponent
	cdef np.ndarray non_labor_weights
	cdef double labor_weight


	#print 'seed weights', sum(seed_weights), seed_weights

	cons = ({'type': 'eq', 'fun': lambda x: 1 - x.sum()})

	bnds = []
	for i in xrange(len(seed_weights)):
		bnds.append((0,1))

	labor_price = prices[0]
	non_labor_prices = prices[1:]
	opt = minimize(F,np.array(seed_weights), args=(np.array(labor_price), np.array(non_labor_prices),cobb_douglas_exponent_labor, cobb_douglas_exponent_non_labor, CES_exponent), method =  'SLSQP', bounds = bnds, constraints = cons, options = {'maxiter':1000000000})


	assert opt.success, opt
	assert  0.999 < opt.x.sum() < 1.001, (opt.x.sum(), opt.x)


	optimal_weights = opt.x
	for weight in optimal_weights:
		assert weight >= 0.000, weight


	#optimal_weights = optimal_weights / (sum(optimal_weights) + float_epsilon)
	optimal_weights = optimal_weights / sum(optimal_weights)

	#assert sum(optimal_weights) == 1.0, (optimal_weights, sum(optimal_weights))



	return optimal_weights













"""
cdef double F(weights, double labor_price, non_labor_prices, double cobb_douglas_exponent_labor, double cobb_douglas_exponent_non_labor, double CES_exponent):
	cdef double value
	cdef double labor_input
	cdef double CES_output
	cdef np.ndarray non_labor_weights
	cdef double labor_weight

	non_labor_weights = weights ** 2 / (1 + weights **2)
	labor_weight = 1 - non_labor_weights.sum()
	non_labor_inputs = non_labor_weights / non_labor_prices
	CES_output = ef.CES(non_labor_inputs, CES_exponent)
	labor_input = labor_weight / labor_price
	value = labor_input ** cobb_douglas_exponent_labor * CES_output ** cobb_douglas_exponent_non_labor
	return -value

def optimize(seed_weights, prices):
	cdef double cobb_douglas_exponent_labor = parameters.cobb_douglas_exponent_labor
	cdef double cobb_douglas_exponent_non_labor = parameters.cobb_douglas_exponent_non_labor
	cdef double CES_exponent = parameters.CES_exponent
	cdef np.ndarray non_labor_weights
	cdef double labor_weight

	labor_price = prices[0]
	non_labor_prices = prices[1:]
	opt = minimize(F,np.array(seed_weights), args=(np.array(labor_price), np.array(non_labor_prices),cobb_douglas_exponent_labor, cobb_douglas_exponent_non_labor, CES_exponent), method =  parameters.weights_optimization_method)

	non_labor_weights = opt.x ** 2 / (1 + opt.x ** 2)
	labor_weight = 1 - non_labor_weights.sum()

	optimal_weights = labor_weight, non_labor_weights
	assert optimal_weights[0] >= 0.000, optimal_weights
	for weight in optimal_weights[1]:
		assert weight >= 0.000, weight
	return optimal_weights
"""


"""
def transform(x):
	cdef double a
	y = x ** 2 / (1 + x **2)
	a = 1 - y.sum()
	return a, y

def F(weights, input_prices, double cobb_douglas_exponent_labor, double cobb_douglas_exponent_non_labor, double CES_exponent):
	cdef double value
	cdef double labor_input
	cdef double CES_output

	weights_tranformed = transform(weights)
	non_labor_inputs = weights_tranformed[1] / input_prices[1:]
	CES_output = ef.CES(non_labor_inputs, CES_exponent)
	labor_input = weights_tranformed[0] / input_prices[0]
	cobb_douglas_quantities = [labor_input, CES_output]
	value = labor_input ** cobb_douglas_exponent_labor * CES_output ** cobb_douglas_exponent_non_labor
	return -value

def optimize(seed_weights, prices):
	cdef double cobb_douglas_exponent_labor = parameters.cobb_douglas_exponent_labor
	cdef double cobb_douglas_exponent_non_labor = parameters.cobb_douglas_exponent_non_labor
	cdef double CES_exponent = parameters.CES_exponent

	opt = minimize(F,np.array(seed_weights), args=(np.array(prices), cobb_douglas_exponent_labor, cobb_douglas_exponent_non_labor, CES_exponent), method =  parameters.weights_optimization_method)
	optimal_weights = transform(opt.x)
	assert optimal_weights[0] >= 0.000
	for weight in optimal_weights[1]:
		assert weight >= 0.000
	return optimal_weights


cdef class WeightsOptimization(object):
	cdef double cobb_douglas_exponent_labor
	cdef double cobb_douglas_exponent_non_labor
	cdef double CES_exponent
	cdef char* method

	def __init__(self):
		self.CES_exponent = parameters.CES_exponent
		#self.cobb_douglas_exponents = parameters.cobb_douglas_exponents
		self.cobb_douglas_exponent_labor = parameters.cobb_douglas_exponent_labor
		self.cobb_douglas_exponent_non_labor = parameters.cobb_douglas_exponent_non_labor
		self.method = parameters.weights_optimization_method

	def transform(self, x):
		cdef double a
		y = x ** 2 / (1 + x **2)
		a = 1 - y.sum()
		return a, y

	def F(self, weights, input_prices):
		cdef double value
		cdef double labor_input
		cdef double CES_output

		weights_tranformed = self.transform(weights)

		non_labor_inputs = weights_tranformed[1] / input_prices[1:]
		CES_output = ef.CES(non_labor_inputs, self.CES_exponent)
		labor_input = weights_tranformed[0] / input_prices[0]
		cobb_douglas_quantities = [labor_input, CES_output]
		value = labor_input ** self.cobb_douglas_exponent_labor * CES_output ** self.cobb_douglas_exponent_non_labor
		return -value

	def optimize(self, seed_weights, prices):
		opt = minimize(self.F,np.array(seed_weights), args=(np.array(prices),), method =  self.method)
		optimal_weights = self.transform(opt.x)
		assert optimal_weights[0] >= 0.000
		for weight in optimal_weights[1]:
			if weight < 0.000:
				print weight
#assert weight >= 0.000
		return optimal_weights

"""

