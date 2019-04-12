import numpy as np
from random import randint

def quicksort(x,l=0,r='a',c=0):
	if r == 'a':
		r = len(x)-1
	if l >= r:
		return x, c
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
	c = c+r-l
	if r-l > 1:
		x1, c1 = quicksort(x,l,i-1,c)
		x2, c2 = quicksort(x1,i+1,r,c1)
		return x, c2
	return x, c

##### Tests
if __name__=='__main__':
	from MergeSort import *
	fname = "LongArray2.txt"
	x=[]
	with open(fname) as f:
		for line in f.readlines():
			x.append(int(line))
	f.close()

	# x=[3,1,5,2,4,14,56,23,21,85,65,95,35]
	cs = []
	for j in range(10**2):
		cs.append(quicksort(x)[1])
	print(mean(cs))
	# print(quicksort(x)[1])