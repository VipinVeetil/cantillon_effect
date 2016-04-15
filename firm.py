"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: firm
	Module description: a firm use a CES function embedded in a Cobb-Douglas function to produce output

"""

from __future__ import division
import economic_functions as ef
import weights_opt
from collections import OrderedDict

class Firm(object):
	def __init__(self):
		self.ID = 0
		""" each firm has a unique ID """
		self.neighbors_IDs = []
		self.cobb_douglas_exponents = []
		""" Cobb-Douglas function has two parameters: labor productivity and non-labor productivity """
		self.CES_exponent = 0
		""" the CES exponent associated with each firm that supplies input """
		self.wealth = 0
		""" nominal wealth of firm over time """
		self.inputs_demand = OrderedDict({})
		""" nominal demand for inputs of different suppliers; index zero is demand for labor input """
		self.inputs = OrderedDict({})
		""" quantity of inputs provided by different suppliers; index zero is quantity of labor input """
		self.inputs_weights = OrderedDict({})
		""" proportion of wealth spend on different inputs """
		self.inputs_prices = OrderedDict({})
		""" prices of different inputs; index zero is wage """
		self.output = 0
		""" output produced by firm over time """
		self.price = 0
		""" price charged by firm over time """
		self.demand = 0
		""" total demand for output in current period """
		self.output_demands = OrderedDict({})
		""" demands from different buyers in current period """
		self.output_allocation = OrderedDict({})
		""" allocation of output to different buyers in current period """
		self.number_of_buyers = 0
	
	def produce(self):
		""" produce output """
		non_labor_inputs = self.inputs.values()[1:]
		""" create list of quantities of non_labor_inputs """
		CES_output = ef.CES(non_labor_inputs, self.CES_exponent)
		""" compute CES portion of output produced using non-labor inputs """
		labor_quantity = self.inputs[0]
		""" quantity of labor is saved as index 0 """
		cobb_douglas_quantities = [labor_quantity, CES_output]
		output = ef.cobb_douglas(cobb_douglas_quantities, self.cobb_douglas_exponents)
		""" compute total output by combining labor and CES_output in a Cobb-Douglas production functions """
		self.output = output
		""" record output  """
	
	def compute_price(self):
		""" compute price of output """
		self.price = self.demand / self.output
		""" price of good is nominal demand divided by real output """
	
	def compute_weights(self):
		""" existing weights are used as seed weights to run optimization algorithm """
		prices = self.inputs_prices.values()
		optimal_weights = weights_opt.optimize(self.seed_weights, prices)
		self.seed_weights = optimal_weights
		count = 0
		for ID in self.neighbors_IDs:
			self.inputs_weights[ID] = optimal_weights[count]
			count += 1

	def allocate_output_to_demanders(self):
		""" allocate the output to different demanders """
		""" the firm does not transfer output to other firms, but records how much to transfer to each buyer in a list """
		for ID in self.output_demands:
			allocation = self.output_demands[ID] / self.price
			""" the quantity of good allocated to each buyer is equal to the demand of the buyer divided by price of the good """
			self.output_allocation.update({ID:allocation})
			""" record the allocation """

	def update_own_demand(self, output_demands):
		""" update the demand for the good produced by the firm; functions takes a dictionary of demands as an argument  """
		self.output_demands = output_demands
		self.demand = sum(self.output_demands.values())

	def update_wealth(self):
		""" sum the demands from different buyers """
		self.wealth = self.demand

	def update_inputs(self, inputs):
		""" update the quantity of inputs recieved from suppliers; functions takes a dictionary of inputs as an argument """
		self.inputs = inputs
	
	def demand_inputs(self):
		""" compute the demand for inputs from different suppliers """
		for ID in self.neighbors_IDs:
			demand = self.inputs_weights[ID] * self.wealth
			""" demand equals the weight associated with an agent multipled by current nominal wealth """
			self.inputs_demand.update({ID: demand})
			