class NHash:
	def __init__(self,prime,r):
		self._hset = set()
		self._repeats = 0
		self._prime = prime

	def get_reps(self):
		return self._repeats

	def add(self,name):
		"""Testing for simple has functions using mod with large primes for storing names"""
		mod = ''
		for i in range(len(name)):
			nmod = 1
			for c in name[i:]:
				nmod = nmod*ord(c) % self._prime
			if nmod == 0:
				nmod = 1
			mod = chr(nmod)+mod 

		nmod = 0
		for c in mod:
			nmod = nmod+ord(c) % self._prime

		if nmod in self._hset:
			self._repeats +=1
		else:
			self._hset.add(nmod)

##### Tests
# if __name__=='__main__':
# 	fname = "first-names.txt"
# 	fname2 = "primes.txt"
# 	primelist = []
# 	with open(fname2) as f:
# 		for line in f.readlines():
# 			line = line.split('\t')
# 			for p in line:
# 				primelist.append(int(p))
# 	f.close()
# 	namelist = []
# 	with open(fname) as f:
# 		for line in f.readlines():
# 			namelist.append(line)
# 	import random
# 	maxp = -1
# 	minp = 50
# 	numnames = len(namelist)
# 	for k in range(200):
# 		r = random.randint(0,10000000)
# 		for i in range(len(namelist)):
# 			# print(i, ((i+20) % len(namelist)), len(namelist))
# 			namelist[i] = namelist[i]+namelist[((i+r) % len(namelist))]

# 		for p in primelist:
# 			NameHash = NHash(p,r)
# 			for name in namelist:
# 				NameHash.add(name)

# 			if NameHash.get_reps() < minp:
# 				minp = NameHash.get_reps()
# 				mininfo = [r,p,NameHash.get_reps(),NameHash.get_reps()/float(numnames)*100.00, numnames]

# 			if NameHash.get_reps() > maxp:
# 				maxp = NameHash.get_reps()
# 				maxinfo = [r,p,NameHash.get_reps(),NameHash.get_reps()/float(numnames)*100.00, numnames]

# 	print(mininfo)
# 	print(maxinfo)



