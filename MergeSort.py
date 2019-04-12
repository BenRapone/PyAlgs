import numpy as np

def Merge(x,y):
	nx = len(x)
	ny = len(y)
	i = 0
	j = 0
	bx = []
	n = nx+ny

	for k in range(n):
		if nx - i == 0:
			bx.append(y[j])
			j += 1
		elif ny - j ==0:
			bx.append(x[i])
			i += 1
		elif x[i] <= y[j]:
			bx.append(x[i])
			i += 1
		else:
			bx.append(y[j])
			j += 1
	return bx

def MergeSort(x):
	n = len(x)
	if n >1:
		return Merge(MergeSort(x[0:n//2]),MergeSort(x[n//2:n]))
		
	else:
		return x

