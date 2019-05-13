

def binary_search(data, target, low=0, high='a'):
	"""Return True if target is found in indicated portion of list"""
	if high == 'a':
		high = len(data)
	if low > high:
		return False
	else:
		mid = (low+high)//2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search(data,target,low, mid-1)
		else:
			return binary_search(data,target,mid+1,high)

def binary_search_it(data,target):
	"""Return True if target is found in indicated portion of list"""
	low = 0
	high = len(data)-1
	while low <= high:
		mid = (low+high)//2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid-1
		else:
			low = mid+1
	return False