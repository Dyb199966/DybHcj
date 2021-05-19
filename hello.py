# import the necessary packages
import numpy as np
 
def chi2_distance(histA, histB, eps = 1e-10):
		# compute the chi-squared distance
	d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
		for (a, b) in zip(histA, histB)])
	Sum = 0;
	for (a,b) in zip(histA, histB):
		E  = ((a - b) ** 2) / (a + b + eps)
		Sum += E
		print Sum/2
	# return the chi-squared distance
	return d
d = chi2_distance([0,1,2,3,4],[4,3,2,1,0])
# print d	