"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
	I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.

	Contact: vipin.veetil@gmail.com

	Language: Python
	
	Module name: analysis
	Module description: analysis the data generated by the simulation
"""

from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import random as random
import numpy as np


def cv_change():
	mean_series =  pd.read_csv('mean_CV_changes.csv')
	max_series =  pd.read_csv('max_CV_changes.csv')
	shocks = np.arange(0,1.01,0.2)
	avg_mean_series = []
	avg_max_series = []
	
	for i in xrange(6):
		series = mean_series.iloc[i][1:]
		avg = np.mean(series)
		avg_mean_series.append(avg)
	
	for i in xrange(6):
		series = max_series.iloc[i][1:]
		avg = np.mean(series)
		avg_max_series.append(avg)

	plt.scatter(shocks, avg_mean_series)
	plt.title('Change in CV of prices', fontsize = 16)
	plt.xlabel('Proportion money injection', fontsize = 14)
	plt.ylabel('Normalized change in coefficient of variation',fontsize = 14)
	plt.grid()
	plt.show()
	
	"""
	plt.scatter(shocks, avg_max_series)
	plt.title('Change in maximum CV of prices', fontsize = 16)
	plt.xlabel('Proportion money injection', fontsize = 14)
	plt.ylabel('Normalized change in maximum coefficient of variation',fontsize = 14)
	plt.grid()
	plt.show()
	"""


cv_change()




def cv_time_series():
	cv =  pd.read_csv('cv_time_series.csv')
	cv =  pd.DataFrame(cv)
	time_steps = range(0,600)
	time_steps = time_steps[450:]
	one_series = cv.iloc[0]
	one_series = list(one_series)[450:]
	two_series = cv.iloc[1]
	two_series = list(two_series)[450:]
	three_series = cv.iloc[2]
	three_series = list(three_series)[450:]
	four_series = cv.iloc[3]
	four_series = list(four_series)[450:]

	plt.plot(time_steps, one_series)
	plt.title('CV prices time series: run 1', fontsize = 16)
	plt.xlim([450,550])
	plt.xlabel('Time steps', fontsize = 14)
	plt.ylabel('Coefficient of variation of prices',fontsize = 14)
	plt.text(504,1.3, '10% money injection at time step 500' ,fontsize = 10,color='black')
	plt.show()

	plt.plot(time_steps, two_series)
	plt.title('CV prices time series: run 2', fontsize = 16)
	plt.xlim([450,550])
	plt.xlabel('Time steps', fontsize = 14)
	plt.ylabel('Coefficient of variation of prices',fontsize = 14)
	plt.text(504,0.9, '10% money injection at time step 500' ,fontsize = 10,color='black')
	plt.show()

	plt.plot(time_steps, three_series)
	plt.title('CV prices time series: run 3', fontsize = 16)
	plt.xlim([450,550])
	plt.xlabel('Time steps', fontsize = 14)
	plt.ylabel('Coefficient of variation of prices',fontsize = 14)
	plt.text(504,22, '10% money injection at time step 500' ,fontsize = 10,color='black')
	plt.show()

	plt.plot(time_steps, four_series)
	plt.title('CV prices time series: run 4', fontsize = 16)
	plt.xlim([450,550])
	plt.xlabel('Time steps', fontsize = 14)
	plt.ylabel('Coefficient of variation of prices',fontsize = 14)
	plt.text(504,1.0, '10% money injection at time step 500' ,fontsize = 10,color='black')
	plt.show()





#cv_time_series()




def price_changes():
	price_changes = pd.read_csv('price_changes.csv')
	price_changes = pd.DataFrame(price_changes)

	one_time = price_changes.iloc[0]
	one_time = list(one_time)
	mean = np.mean(one_time)
	print 'mean one', mean
	print 'max one', max(one_time)
	one_time.remove(max(one_time))

	two_time = price_changes.iloc[1]
	two_time = list(two_time)
	mean = np.mean(two_time)
	print 'mean two', mean
	print 'max two', max(two_time)
	two_time.remove(max(two_time))

	three_time = price_changes.iloc[2]
	three_time = list(three_time)
	mean = np.mean(three_time)
	print 'mean three', mean
	print 'max three', max(three_time)
	three_time.remove(max(three_time))

	four_time = price_changes.iloc[3]
	four_time = list(four_time)
	mean = np.mean(four_time)
	print 'mean four', mean
	print 'max four', max(four_time)
	four_time.remove(max(four_time))

	five_time = price_changes.iloc[4]
	five_time = list(five_time)
	mean = np.mean(five_time)
	print 'mean five', mean
	print 'max five', max(five_time)
	five_time.remove(max(five_time))

	ten_time = price_changes.iloc[5]
	ten_time = list(ten_time)
	mean = np.mean(ten_time)
	print 'mean ten', mean
	print 'max ten', max(ten_time)
	ten_time.remove(max(ten_time))

	twenty_time = price_changes.iloc[6]
	twenty_time = list(twenty_time)
	mean = np.mean(twenty_time)
	print 'mean twenty', mean
	print 'max twenty', max(twenty_time)
	twenty_time.remove(max(twenty_time))

	fifty_time = price_changes.iloc[7]
	fifty_time = list(fifty_time)
	mean = np.mean(fifty_time)
	print 'mean fifty', mean
	print 'max fifty', max(fifty_time)
	fifty_time.remove(max(fifty_time))



	one_time_price_decrease = 0
	mean_decrease = []
	for price_change in one_time:
		if price_change < -0.000000001:
			one_time_price_decrease += 1

	one_time_price_decrease = (one_time_price_decrease / len(one_time))
	print one_time_price_decrease, 'one_time_price_decrease'

	two_time_price_decrease = 0
	for price_change in two_time:
		if price_change < -0.000000001:
			two_time_price_decrease += 1
	two_time_price_decrease = (two_time_price_decrease / len(two_time))
	print two_time_price_decrease, 'two_time_price_decrease'



	three_time_price_decrease = 0
	for price_change in three_time:
		if price_change < -0.000000001:
			three_time_price_decrease += 1
	three_time_price_decrease = (three_time_price_decrease / len(three_time))
	print three_time_price_decrease, 'three_time_price_decrease'

	four_time_price_decrease = 0
	for price_change in four_time:
		if price_change < -0.000000001:
			four_time_price_decrease += 1
	four_time_price_decrease = (four_time_price_decrease / len(four_time))
	print four_time_price_decrease, 'four_time_price_decrease'

	five_time_price_decrease = 0
	for price_change in five_time:
		if price_change < -0.000000001:
			five_time_price_decrease += 1
	five_time_price_decrease = (five_time_price_decrease / len(five_time))
	print five_time_price_decrease, 'five_time_price_decrease'

	ten_time_price_decrease = 0
	for price_change in ten_time:
		if price_change < -0.000000001:
			ten_time_price_decrease += 1
	ten_time_price_decrease = (ten_time_price_decrease / len(ten_time))
	print ten_time_price_decrease, 'ten_time_price_decrease'

	twenty_time_price_decrease = 0
	for price_change in twenty_time:
		if price_change < -0.000000001:
			twenty_time_price_decrease += 1
	twenty_time_price_decrease = (twenty_time_price_decrease / len(twenty_time))
	print twenty_time_price_decrease, 'twenty_time_price_decrease'

	fifty_time_price_decrease = 0
	for price_change in fifty_time:
		if price_change < -0.000000001:
			fifty_time_price_decrease += 1
	fifty_time_price_decrease = (fifty_time_price_decrease / len(fifty_time))
	print fifty_time_price_decrease, 'fifty_time_price_decrease'



	plt.hist(one_time, 100, weights=np.zeros_like(one_time) + 1. / len(one_time))
	plt.title('Distribution of price differences after one time step', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(5,0.85, '0.00 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()


	plt.hist(three_time, 100, weights=np.zeros_like(three_time) + 1. / len(three_time))
	plt.title('Distribution of price differences after three time steps', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(0.5,0.36, '0.02 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()



	plt.hist(five_time, 100, weights=np.zeros_like(five_time) + 1. / len(five_time))
	plt.title('Distribution of price differences after five time steps', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(0, 0.37, '0.05 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()


	plt.hist(fifty_time, 100, weights=np.zeros_like(fifty_time) + 1. / len(twenty_time))
	plt.title('Distribution of price differences after fifty time steps', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(-0.1,0.85, '0.004 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()

	"""

	plt.hist(two_time, 100, weights=np.zeros_like(two_time) + 1. / len(two_time))
	plt.title('Distribution of price differences after two time steps', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(8,0.52, '0.01 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()

	plt.hist(four_time, 100, weights=np.zeros_like(four_time) + 1. / len(four_time))
	plt.title('Distribution of price differences after four time steps', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(1,0.31, '0.04 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()

	plt.hist(ten_time, 100, weights=np.zeros_like(ten_time) + 1. / len(ten_time))
	plt.title('Distribution of price differences after ten time steps', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(2,0.82, '0.05 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()


	plt.hist(twenty_time, 100, weights=np.zeros_like(twenty_time) + 1. / len(twenty_time))
	plt.title('Distribution of price differences after twenty time steps', fontsize = 16)
	plt.xlabel('Normalized price differences', fontsize = 14)
	plt.ylabel('Proportion of firms',fontsize = 14)
	plt.text(-0.10,0.55, '0.005 proportion of firms have lower price' ,fontsize = 12,color='black')
	plt.grid()
	plt.show()

	"""



