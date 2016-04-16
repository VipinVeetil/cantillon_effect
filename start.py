"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: Start
	Module description: starts a single run of simulation
	
"""
from __future__ import division
import run
import random
import matplotlib.pyplot as plt
from operator import add
import parameters
from time import time
import numpy as np

t = time()
class Start(object):

	def __init__(self):
		self.run = run.Run()

	def create_economy(self):
		self.run.create_economy()

	def forward_in_time(self):
		self.run.time_steps()



start_instance = Start()
""" instantiate start """
start_instance.create_economy()
""" create economy """
start_instance.forward_in_time()
""" run it forward in time """

print (time() - t), "seconds", parameters.number_of_firms, "firms", parameters.time_steps, "time steps"
print (time() - t)/60, "minutes", parameters.number_of_firms, "firms", parameters.time_steps, "time steps"
print (time() - t)/3600, "hours", parameters.number_of_firms, "firms", parameters.time_steps, "time steps"




plt.plot(start_instance.run.prices_mean)
plt.title('Mean Price')
plt.show()


plt.plot(start_instance.run.output)
plt.title('Output')
plt.show()


plt.plot(start_instance.run.output[30:])
plt.title('Last Output')
plt.show()


"""

plt.plot(start_instance.run.GDP)
plt.title('Nominal GDP')
plt.show()


real_GDP = []
for i in xrange(len(start_instance.run.GDP)):
	real = start_instance.run.GDP[i] / start_instance.run.prices_mean[i]
	real_GDP.append(real)


plt.plot(real_GDP)
plt.title('Real GDP')
plt.show()


plt.plot(real_GDP[30: ])
plt.title('Last Real GDP')
plt.show()













plt.plot(start_instance.run.wealth_cv)
plt.title('Firms Wealth CV')
plt.show()


plt.plot(start_instance.run.prices_cv)
plt.title('CV price')
plt.show()



plt.plot(start_instance.run.economy.household.wealth)
plt.title('Household Wealth')
plt.show()


real_GDP = np.array(start_instance.run.GDP) / (parameters.number_of_firms + 1)
plt.plot(real_GDP)
plt.title('Real GDP')
plt.show()

"""

