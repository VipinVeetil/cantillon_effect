"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: Time Step
	Module description: the events that happen every time step; input-output network is bi-directional
	
"""
from __future__ import division
import random
from collections import OrderedDict

class TimeStep(object):
	def __init__(self):
		self.economy = None
	
	def firms_produce(self):
		""" firms transform inputs into output """
		for firm in self.economy.firms_list:
			firm.produce()

	def agents_compute_demand_goods(self):
		""" firms and household compute the demand for their respective inputs """
		for firm in self.economy.firms_list:
			firm.demand_inputs()
		self.economy.household.demand_goods()

	def firms_compute_prices(self):
		""" firms compute prices of their respective output """
		for firm in self.economy.firms_list:
			firm.compute_price()

	def firms_compute_weights(self):
		""" firms compute the proportions in which to buy inputs from sellers """
		number_of_firms = int(self.economy.number_of_firms * self.economy.percent_firms_change_weights)
		firms_which_change_weights = random.sample(self.economy.firms_list, number_of_firms)
		for firm in firms_which_change_weights:
			firm.compute_weights()

	def household_compute_wage(self):
		""" household computes wage """
		self.economy.household.compute_wage()

	def transfer_price_information(self):
		""" each firm recieves information about the price of its inputs """
		for firm in self.economy.firms_list:
			prices_dictionary = OrderedDict({})
			prices_dictionary.update({0:self.economy.household.wage[-1]})
			suppliers = self.economy.firms_network.neighbors(firm)
			for supplier in suppliers:
				prices_dictionary.update({supplier.ID:supplier.price})
			firm.inputs_prices = prices_dictionary

	def transfer_demand_information(self):
		""" transfer information about demands for their outputs to firms and households """
		labor_demands = OrderedDict({})
		""" a dictionary to record labor demanded by different firms """
		for firm in self.economy.firms_list:
			labor_demands.update({firm.ID: firm.inputs_demand[0]})
			""" update labor demand with the quantity of labor demanded by the firm """
			demands_dictionary = {}
			demands_dictionary.update({0: self.economy.household.goods_demand[firm.ID]})
			""" a dictionary to record demand for a firms output """
			demanders = self.economy.firms_network.neighbors(firm)
			""" the predecessors of a firm demand its output """
			for demander in demanders:
				demands_dictionary.update({demander.ID: demander.inputs_demand[firm.ID]})
			firm.update_own_demand(demands_dictionary)
			""" pass information about the demand for the firms output """
		self.economy.household.update_labor_demand(labor_demands)
		""" pass information about labor demand to household """

	def allocate_inputs(self):
		""" each firm allocates its output to different demanders; allocation is done according to nominal demand and price """
		for firm in self.economy.firms_list:
			firm.allocate_output_to_demanders()
		self.economy.household.allocate_labor()
		""" household allocates labor to different firms; allocation is done according to nominal demand for labor and wage """

	def transfer_inputs(self):
		""" transfer inputs to different firm according to the allocation made by "allocate_inputs" function """
		for firm in self.economy.firms_list:
			labor = self.economy.household.labor_allocation[firm.ID]
			""" the quantity of labor allocated to the firm """
			firm.inputs.update({0:labor})
			""" firm updates labor available to it """
			suppliers = self.economy.firms_network.neighbors(firm)
			""" successors of a firm are its suppliers because direction indicates flow of money, goods flow in the opposite direction """
			for supplier in suppliers:
				input = supplier.output_allocation[firm.ID]
				firm.inputs.update({supplier.ID:input})
				""" give firm the quantity of inputs provided by different suppliers """

	def transfer_consumption_good(self):
		""" transfer consumption good to household """
		for firm in self.economy.firms_list:
			consumption_good = firm.output_allocation[0]
			self.economy.household.goods.update({firm.ID:consumption_good})

	def update_wealth(self):
		""" firms update wealth """
		for firm in self.economy.firms_list:
			firm.update_wealth()
		self.economy.household.update_wealth()
		""" household updates wealth """

	def compute_welfare(self):
		""" economy wide welfare is simply the utility of the representative household """
		self.economy.household.compute_utility()




