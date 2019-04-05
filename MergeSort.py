import numpy as np

def Merge(x,y):
	nx = len(x)
	ny = len(y)
	if ny == 0:
		return x
	if nx == 0:
		return y
	if x[0] <= y[0]:
		return np.concatenate((x[0], Merge(x[1:nx],y)), axis=None)
	else:
		return np.concatenate((y[0], Merge(x,y[1:ny])), axis=None)

def MergeSort(x):
	n = len(x)
	if n >1:
		return Merge(MergeSort(x[0:n//2]),MergeSort(x[n//2:n]))
	else:
		return x

