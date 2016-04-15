"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: Run
	Module description: create an economy and run the different functions that define a time step
	
"""

from __future__ import division
import economy
import time_step as ts
import parameters
import scipy.stats as stats
import numpy as np

class Run(object):
	def __init__(self):
		self.economy = economy.Economy()
		self.time_step = ts.TimeStep()
		self.number_time_steps = parameters.time_steps
		self.wealth = []
		self.wealth_cv = []
		""" the coefficient of variation of wealth among firms """
		self.prices_mean = []
		self.prices_cv = []
		""" the coefficient of variation of prices charged by firms """
	
	def create_economy(self):
		self.economy = economy.Economy()
		self.time_step = ts.TimeStep()
		self.economy.create_firms()
		""" create firms """
		self.economy.create_firms_network()
		""" place the firms in a network """
		""" firms must be placed in network before creating household because those firms that do not have predessors become retail firm and are assigned to household for supply of consumption good """
		self.economy.create_household()
		""" create household """
		self.economy.assign_initial_inputs_weights()
		""" assign initial weights that define the proportions in which firms buy inputs from each other """
		self.economy.assign_initial_inputs()
		""" assign each firm random quantities of initial inputs """
	
	def record_statistics(self):
		""" record data as system runs forward in time """
		wealth = []
		prices = []
		for firm in self.economy.firms_list:
			wealth.append(firm.wealth)
			prices.append(firm.price)
		self.wealth.append(sum(wealth))
		self.wealth_cv.append(stats.variation(wealth))
		self.prices_mean.append(np.mean(prices))
		self.prices_cv.append(stats.variation(prices))

	def time_steps(self):
		self.time_step.economy = self.economy
		""" assign the economy to functions that occur every time step """
		for time in xrange(self.number_time_steps):
			if time % 1 == 0:
				print time, "time step"
			self.time_step.firms_produce()
			""" produce """
			self.time_step.agents_compute_demand_goods()
			""" compute demand for others goods """
			self.time_step.transfer_demand_information()
			""" pass demand information """
			self.time_step.update_wealth()
			""" update wealth """
			self.time_step.firms_compute_prices()
			""" use demand information to compute prices """
			self.time_step.household_compute_wage()
			""" use demand information to compute wage """
			self.time_step.transfer_price_information()
			""" transfer price information """
			self.time_step.allocate_inputs()
			""" allocate inputs to each others using demand information and prices """
			self.time_step.transfer_inputs()
			""" transfer inputs to each other """
			self.time_step.transfer_consumption_good()
			""" retail firms transfer consumption good to household """
			self.time_step.compute_welfare()
			""" compute household welfare """
			self.time_step.firms_compute_weights()
			self.record_statistics()
			""" record economy statistics """



