"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: economic functions
	Module description: functions that are commonly used in economics.

"""

from __future__ import division
import math
import copy
import random
cimport numpy as np
import numpy as np



cpdef double cobb_douglas(variables_list, exponents_list):
	""" Cobb-Douglas Function """
	variables_list = np.array(variables_list)
	#exponents_list = np.array(exponents_list)
	return (variables_list ** exponents_list).prod()


cpdef double CES(variables_list, exponent):
	value = (np.power(variables_list, exponent).sum()) ** (1.0 / exponent)
	return value


def incremental_value(variables_list, exponents_list, which_variable, incremental_quantity, which_function):
	""" the change in the value of a function from a change in one of its variables """
	""" the discrete version of marginal product/marginal utility, with the discrete unit as an argument """
	if which_function == "Cobb-Douglas":
		new_variables_list = copy.copy(variables_list)
		assert which_variable < len(variables_list), "variable not in list"
		new_variables_list[which_variable] += incremental_quantity
		""" new list of variables with an additional unit of one of the variables """
		
		value_increment = cobb_douglas(new_variables_list, exponents_list) - cobb_douglas(variables_list, exponents_list)
		""" new value with additional unit of a variable minus old value """
		return value_increment

def geometric_brownian_motion_single_value(drift, volatility, initial_value):
	dt = 1
	new_value = initial_value * math.exp((drift - ((volatility ** 2) / 2.0) * dt + volatility * random.normalvariate(0, dt * dt)))
	return new_value

def normalized_random_numbers(how_many):
	random_numbers = np.random.random((how_many,))
	sum_random_numbers = sum(random_numbers)
	normalized = random_numbers / sum_random_numbers
	return normalized


def random_numbers(how_many):
	random_numbers = np.random.random((how_many,))
	return random_numbers






