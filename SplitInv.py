import numpy as np
import random

def Merge_InvCount(x,y,count):
	nx = len(x)
	ny = len(y)
	if ny == 0:
		return x, count
	if nx == 0:
		return y, count
	if x[0] <= y[0]:
		lx, lcount = Merge_InvCount(x[1:nx],y,count)
		return np.concatenate((x[0], lx), axis=None), lcount
	else:
		ly, lcount = Merge_InvCount(x,y[1:ny],count+nx)
		return np.concatenate((y[0],ly), axis=None), lcount

def MergeSort_InvCount(x,count=0):
	n = len(x)
	if n >1:
		xl, nl = MergeSort_InvCount(x[0:n//2],count)
		xh, nh = MergeSort_InvCount(x[n//2:n],count)
		return Merge_InvCount(xl,xh,nl+nh)
	else:
		return x, count

