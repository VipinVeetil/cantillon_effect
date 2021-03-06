
"""
	Please feel free to use the code without citing or crediting me.
	Cheers to science :-)
	I'd be happy to hear from you about how to improve this code.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Code language: Python
	
	Module name: parameters
	Module description: parameters of the model
	
"""

from __future__ import division
import numpy as np


number_of_firms = 50
time_steps = 1000
labor = 1000
barabasi_albert_graph_parameter = 2


CES_exponent = 0.8
cobb_douglas_exponent_labor = 0.3
cobb_douglas_exponent_non_labor = 0.7
cobb_douglas_exponents = [cobb_douglas_exponent_labor, cobb_douglas_exponent_non_labor]
percent_firms_change_weights = 1