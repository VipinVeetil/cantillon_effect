"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: representative household
	Module description: representative household consumers goods, supplies labor, and receives labor income

"""

from __future__ import division
import fast_economic_functions as ef

class Household(object):
	
	def __init__(self):
		self.ID = 0
		self.wealth = []
		self.wage = []
		self.labor_supply = 1
		self.labor_demand_sum = 0
		""" sum of nominal labor demand by all firms """
		self.labor_demand = {}
		self.utility = []
		self.utility_function_parameters = {}
		"""
			the keys of the dictionary are the firm IDs
			the values are the exponents associated with each firms' output in the a Cobb-Douglas utility functions
			
		"""
		self.goods = {}
		"""
			the keys of the dictionary are the firm IDs
			the values are the quantity of goods bought from each associated firm
			
		"""
		self.goods_demand = {}
		""" the households nominal demand for the different consumption goods """
		self.labor_allocation = {}
		""" quantity of labor allocated to different firms """
	
	def compute_wage(self):
		""" compute wage """
		wage = self.labor_demand_sum /  self.labor_supply
		""" wage equals nominal labor demand divided by labor supply """
		self.wage.append(wage)
		""" record wage """
	
	def update_goods(self, goods):
		""" record consumption goods bought from firms """
		self.goods = goods
	
	def compute_utility(self):
		utility = ef.cobb_douglas(self.goods.values(), self.utility_function_parameters.values())
		""" python dict.values() produces lists that are ordered according to keys
			since the keys of both self.goods and self.utility_function_parameters are firm IDs
			the two lists of keys order quantity of goods and exponents correspondingly
		"""
		self.utility.append(utility)
	
	def update_wealth(self):
		self.wealth.append(self.labor_demand_sum)
		""" household nominal wealth equals nominal labor demand """

	def demand_goods(self):
		""" compute nominal demand for different goods """
		for firm_ID in self.utility_function_parameters:
			demand = self.utility_function_parameters[firm_ID] * self.wealth[-1]
			""" nominal demand for a good equals wealth times Cobb-Douglas exponent """
			self.goods_demand.update({firm_ID:demand})

	def update_labor_demand(self, demands):
		self.labor_demand = demands
		""" dictionary of labor demand of different firms """
		self.labor_demand_sum = sum(demands.values())
		""" total nominal labor demand """

	def allocate_labor(self):
		""" allocate labor to different firms """
		for firm_ID in self.labor_demand:
			quantity_of_labor = self.labor_demand[firm_ID] / self.wage[-1]
			""" quantity of labor allocated to each firm equals its demand divided by wage """
			self.labor_allocation.update({firm_ID:quantity_of_labor})











