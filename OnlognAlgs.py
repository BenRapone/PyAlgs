
def unique(S):
	""" Return True if there are no duplicate elements in sequence S"""
	temp = sorted(S)
	for j in range(1,len(temp)):
		if S[j-1] == S[j]:
			return False
	return True