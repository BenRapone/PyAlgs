import numpy as np
from random import randint

def quicksort(x,l=0,r='a'):
	"""quick sort alg recursively defined using randomized median pivot choice from 3 elements"""
	if r == 'a':
		r = len(x)-1
	if l >= r:
		return x
		
	m = randint(l,r)
	meds = dict()
	meds[x[m]] = m
	meds[x[l]] = l
	meds[x[r]] = r
	i = meds[np.median([x[m],x[l],x[r]])]
	x[l], x[i] = x[i], x[l]
	p = x[l] 
	i = l
	for j in range(l+1,r+1):
		if x[j] <= p:
			i = i+1
			x[j], x[i] = x[i], x[j]
			

	x[l], x[i] = x[i], x[l]
	quicksort(x,l,i-1)
	quicksort(x,i+1,r)
	return x

