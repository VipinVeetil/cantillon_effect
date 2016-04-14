"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: economy
	Module description: economic consists of firms and representative household; firms are on a bi-directional network, i.e. the suppliers of a firms inputs are also the buyers of its output

"""

from __future__ import division
import parameters
import firm
import household
import networkx as nx
import random
import economic_functions as ef
from collections import OrderedDict

class Economy(object):
	def __init__(self):
		""" a collection of commonly used functions in economics """
		self.firm = firm
		""" class firm """
		self.labor = parameters.labor
		""" quantity of labor supplied by representative household """
		self.number_of_firms = parameters.number_of_firms
		""" number of firms in the economy """
		self.percent_firms_change_weights = parameters.percent_firms_change_weights
		""" percent of firms which changes weights every time step """
		self.firms_list = []
		""" a list of all firms in the economy """
		self.firms_network = None
		""" network of firms """
		self.household = None
		""" representative household """
		self.CES_exponent = parameters.CES_exponent
		self.cobb_douglas_exponents = parameters.cobb_douglas_exponents
		""" parameters of production function used by firms """
		self.barabasi_albert_graph_parameter = parameters.barabasi_albert_graph_parameter
		""" parameter used to construct Scale-free bi-directional network using networkx """
	
	def create_firms(self):
		self.firms_list = [self.firm.Firm() for count in xrange(self.number_of_firms)]
		""" instantiate a number of firms """
		ID = 1
		""" firm IDs begin from 1 because the household has ID 0 """
		for firm in self.firms_list:
			firm.wealth = random.uniform(0,1)
			""" assign random initial wealth to each firm """
			firm.price = random.uniform(0,1)
			""" assign random initial price to each firm """
			firm.CES_exponent = self.CES_exponent
			""" assign CES production exponent to each firm """
			firm.cobb_douglas_exponents = self.cobb_douglas_exponents
			""" assign cobb-douglas exponents to each firm """
			firm.ID = ID
			""" assign firm ID """
			ID += 1
			""" increment ID by one so that each firm gets a different ID """

	def create_household(self):
		self.household = household.Household()
		""" instantiate a representative household """
		self.household.wealth.append(random.uniform(0,1))
		""" assign random initial wealth to household """
		self.household.wage.append(random.uniform(0,1))
		""" assign random initial wage to household """
		self.household.labor = self.labor
		""" assign quantity of labor supplied to household """
		self.household.labor_demand_sum = random.uniform(0,1)
		""" assign random initial nominal demand for labor """
		exponents = ef.normalized_random_numbers(self.number_of_firms)
		""" the function generates a list of normalized random numbers; length of list is the argument """
		""" the list is the Cobb-Douglas exponents of the household utility function """
		""" household buys goods only from retail firms, so it as has many exponents as there are retail firms """
		count = 0
		for firm in self.firms_list:
			""" assign an Cobb-Douglas exponent for each good supplied by firms """
			self.household.utility_function_parameters.update({firm.ID: exponents[count]})
			count += 1
					
	def create_firms_network(self):
		G = nx.barabasi_albert_graph(self.number_of_firms, self.barabasi_albert_graph_parameter)
		mapping = dict(enumerate(self.firms_list))
		self.firms_network = nx.relabel_nodes(G, mapping)
		""" replace the nodes in the graph with firms """
		

	def assign_initial_inputs_weights(self):
		""" make the input-output network a weighted network """
		""" the weights represent the proportions in which firms buy inputs from their suppliers """
		for firm in self.firms_list:
			suppliers = self.firms_network.neighbors(firm)
			number_of_suppliers = len(suppliers)
			how_many_random_numbers = number_of_suppliers + 1
			""" generate a list of normalize random numbers of lenght one more than number of supplier firms, because labor is an input for all firms """
			weights = ef.normalized_random_numbers(how_many_random_numbers)
			""" the weights are normalized random numbers """
			inputs_weights = OrderedDict({0:weights[0]})
			""" the input weight 0th position is labor weight because household is represented by 0 """
			count = 1
			neighbors_IDs = [0]
			for supplier in suppliers:
				inputs_weights.update({supplier.ID: weights[count]})
				""" assign an input weight for each of the suppliers """
				count += 1
				neighbors_IDs.append(supplier.ID)
			firm.inputs_weights = inputs_weights
			firm.neighbors_IDs = neighbors_IDs
			firm.seed_weights = weights
		""" assign the firm input weights """

	def assign_initial_inputs(self):
		""" assign each firm a quantity of initial input """
		for firm in self.firms_list:
			firm.inputs.update({0: random.uniform(0,1)})
			""" index 0 indicates initial quantity of labor available to the firm """
			suppliers = self.firms_network.neighbors(firm)
			""" make a list of suppliers of the firm; successors are suppliers of inputs because direction indicates flow of money, goods flow in opposite direction """
			for supplier in suppliers:
				firm.inputs.update({supplier.ID: random.uniform(0,1)})
				""" for each supplier of inputs to the firm assign a random initial quantity """

