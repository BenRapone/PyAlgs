import os 

def prefix_average(S):
	"""Return list such that, for all j, A[j] equals average of S[0],S[1],...,S[j]"""
	n=len(S)
	A=[]
	total = 0
	for j in range(n):
		total += S[j]
		A.append(total / (j+1))
	return A

def disk_usage(path):
	"""Return the number of butes used by a file/folder and any descendents."""
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			childpath = os.path.join(path, filename)
			total += disk_usage(childpath)

	# print('{0:<7'.format(total), path)
	return total

def fibonacci(n):
	"""Return pair of Fibonacci numbers, F(n) and F(n-1)"""
	if n<=1:
		return(n,0)
	else:
		(a,b) = fibonacci(n-1)
		return (a+b,a)

def linear_sum(S,start,n,init=True):
	"""Return the sum of n consecutive entries starting from start index of S"""
	if init:
		n = start+n
		init = False
	if n == start:
		return 0
	else:
		return linear_sum(S,start,n-1,init)+S[n-1]

def reverse(S,start,stop):
	"""Reverse elements in implicit slice S[start:stop]"""
	if start<stop-1:
		S[start], S[stop-1] = S[stop-1], S[start]
		reverse(S,start+1,stop-1)

def reverse_it(S):
	"""Reverse elements in implicit slice S[start:stop]"""
	start,stop = 0, len(S)
	while start < stop-1:
		S[start], S[stop-1] = S[stop-1], S[start]
		start, stop = start+1, stop-1