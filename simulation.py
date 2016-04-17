"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
	I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.

	Contact: vipin.veetil@gmail.com
	
	Language: Python
	
	Module name: simulations
	Module description: runs the economy many times
"""

from __future__ import division
import run
import parameters
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy import stats

class Simulation(object):
	def __init__(self):
		self.run = None
		self.monetary_shock_percent = 0.1
		self.number_of_cv_time_series = 4
	
	def assign_parameter_values(self):
		parameters.monetary_shock_percent = self.monetary_shock_percent

	def create_economy(self):
		self.run = run.Run()
		self.run.create_economy()

	def forward_in_time(self):
		self.run.time_steps()

	def simulations(self):
		increment_monetary_shock_percent = 0.01
		monetary_shock_percent_list = np.arange(0.00, 1.01, increment_monetary_shock_percent)
		with open('monetary_shocks.csv', 'wb') as monetary_shocks:
			for percent_shock in monetary_shock_percent_list:
				print 'percent_shock', percent_shock
				self.monetary_shock_percent = percent_shock
				self.assign_parameter_values()
				self.create_economy()
				self.forward_in_time()
				mean_CV = np.mean(self.run.prices_cv[500:600])
				max_CV = max(self.run.prices_cv[500:600])
				writer = csv.writer(monetary_shocks, delimiter=',')
				writer.writerow([percent_shock] + [mean_CV] + [max_CV])


	def simulations_price_changes(self):
		self.assign_parameter_values()
		self.create_economy()
		self.forward_in_time()
		time_differences = [1,2,3,4,5,10,20,50]
		with open('price_changes.csv', 'wb') as price_changes:
			for time in time_differences:
				histogram_data = []
				print time, 'time difference'
				for firm in self.run.economy.firms_list:
					percent_price_change = (firm.price_series[499 + time] - firm.price_series[499]) / firm.price_series[499]
					histogram_data.append(percent_price_change)
				writer = csv.writer(price_changes, delimiter=',')
				writer.writerow([time] + histogram_data)

	def simulations_cv_time_series(self):
		with open('cv_time_series.csv', 'wb') as cv_time_series:
			for number in xrange(self.number_of_cv_time_series):
				print number
				self.assign_parameter_values()
				self.create_economy()
				self.forward_in_time()
				series = self.run.prices_cv
				writer = csv.writer(cv_time_series, delimiter=',')
				writer.writerow(series)










simulation_instance = Simulation()
#simulation_instance.simulations()
#simulation_instance.simulations_price_changes()
simulation_instance.simulations_cv_time_series()
