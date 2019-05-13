import numpy as np

def InvCount_Merge(x,y,count):
	"""Inversion counter piggy back on merge sort"""
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
			count +=  nx-i
	return bx, count


def InvCount(x, count =0):
	n = len(x)
	if n >1:
		xx, nx = InvCount(x[0:n//2],count)
		xy, ny = InvCount(x[n//2:n],count)
		return InvCount_Merge(xx,xy,nx+ny)
		
	else:
		return x, count




