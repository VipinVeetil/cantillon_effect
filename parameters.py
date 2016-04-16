
"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: parameters
	Module description: parameters of the model
	
"""

from __future__ import division


number_of_firms = 1000
time_steps = 1000
CES_exponent = 0.8
cobb_douglas_exponents = [0.3, 0.7]
labor = 1000
barabasi_albert_graph_parameter = 1
percent_firms_change_weights = 0.1
weights_endogeneous = True


money_stock = number_of_firms + 1
monetary_shock_time_step = int(time_steps/2)
monetary_shock_type = 'positive'
monetary_shock_percent = 0.1
proportion_firms_monetary_injection = 0.01
number_firms_monetary_injection = int(proportion_firms_monetary_injection * number_of_firms)