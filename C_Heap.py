class C_Heap:

	def __init__(self, l=[]):
		self.heap = []
		if l != []:
			for v in l:
				self.heap.insert(v)
		

	def self(self,vpos = -48):
		if vpos == -48:
			return self.heap
		elif vpos >= len(self.heap):
			return None
		else:
			return self.heap[vpos]

	def index(self, v):
		return self.heap.index(v)

	def len(self):
		return len(self.heap)

	def insert(self,v):
		""" v is a tuple with v[1] the tie breaker variable (larger v[1] takes priority). Keep the root at the 0 position to take advantage of list append and pop """
		self.heap.append(v) #### Append new vertex at end of list/tree
		vpos = len(self.heap)-1 ### Initiate position of newly added vtx
		balanced = False ### Initiate status of unbalanced tree
		while not balanced:
			if vpos == 0 or self.heap[(vpos+1)//2-1][0] < self.heap[vpos][0]: ### stop loop if the newly added vertex is at the root or parent is smaller
				balanced = True
			elif self.heap[(vpos+1)//2-1][0] > self.heap[vpos][0] or self.heap[(vpos+1)//2-1][1] < self.heap[vpos][1]: ### swap parent/child if parent > child or if == but with lesser weight
				self.heap[(vpos+1)//2-1], self.heap[vpos] = self.heap[vpos], self.heap[(vpos+1)//2-1]
				vpos = (vpos+1)//2-1
			else:  ### Finaly case is par == child and p_weight > c_weight 
				balanced =True

	def pop(self):
		if self.heap == []: ### if the heap is empty return none
			return None
		root = self.heap[0] ### if the heap is not empty identify root
		if len(self.heap) == 1: ### if the heap has only the root then empty and return root
			self.heap = []
			return root
		
		self.heap[0] = self.heap[-1] ### if the heap has at least 2 elements swap the bottom most node with the root
		del self.heap[-1] ### delete the root in its new position
		if len(self.heap) == 1: ### if the heap has only the root left then return root
			return root

		vpos = 0 ### Identify the position of the potentially unbalanced new node at the root
		balanced = False ### initialize state that the tree is unbalanced
		# oldpos = -1 ### initialize oldposition of 
		while not balanced:
			if (vpos+1)*2 -1 >= len(self.heap): ### if the unbalanced node is at the bottom of the tree then stop
				balanced =True
				return root

			elif (vpos+1)*2 -1 == len(self.heap)-1: ### if the unbalanced node has only one child (necessarily the left) check it
				if self.heap[vpos][0] < self.heap[(vpos+1)*2-1][0]: ### if the parent < child then stop and return root
					balanced = True
					return root
				elif self.heap[vpos][0] > self.heap[(vpos+1)*2-1][0] or self.heap[vpos][1] < self.heap[(vpos+1)*2-1][1]: ### if parent> child or (p=c and p_weight<p_child) then swap 
					self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
					vpos = (vpos+1)*2-1
				else: ### last case p=c and p_weight > p_child => stop and return root
					balanced = True
					return root

			else: ### parent has 2 children and we will swap with smallest child if necessary
				if self.heap[vpos][0] < min(self.heap[(vpos+1)*2-1][0], self.heap[(vpos+1)*2][0]): ## if parent < both children then stop and return root
					balanced = True
					return root
				elif self.heap[vpos][0] == min(self.heap[(vpos+1)*2-1][0], self.heap[(vpos+1)*2][0]): ## if parent == min(children) find min and compare
					if self.heap[(vpos+1)*2-1][0] < self.heap[(vpos+1)*2][0]: ## if parent = lchild < rchild 
						if self.heap[vpos][1] < self.heap[(vpos+1)*2-1][1]: ### if p_weight < lc_weight swap
							self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
							vpos = (vpos+1)*2-1
						else: ### par=lchild < rchild and p_weight >= lc_weight thus stop and return root
							balanced = True
							return root
					elif self.heap[(vpos+1)*2][0] < self.heap[(vpos+1)*2-1][0]: ## if parent = rchild < lchild 
						if self.heap[vpos][1] < self.heap[(vpos+1)*2][1]: ### if p_weight < rc_weight swap
							self.heap[vpos], self.heap[(vpos+1)*2] = self.heap[(vpos+1)*2], self.heap[vpos]
							vpos = (vpos+1)*2
						else: ### par=rchild < lchild and p_weight >= rc_weight thus stop and return root
							balanced = True
							return root
					else: ### children are the same so check weights
						if self.heap[(vpos+1)*2-1][1] >= self.heap[(vpos+1)*2][1]: ### if lc_weight > rc_weight then check lc
							if self.heap[vpos][1] < self.heap[(vpos+1)*2-1][1]: ### if p_weight < lc_weight then swap
								self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
								vpos = (vpos+1)*2-1
							else: ## if p_weight >= lc_weight >= rc_weight then stop and return root
								balanced = True
								return root
						else:
							if self.heap[vpos][1] < self.heap[(vpos+1)*2][1]: ### if p_weight < rc_weight then swap
								self.heap[vpos], self.heap[(vpos+1)*2] = self.heap[(vpos+1)*2], self.heap[vpos]
								vpos = (vpos+1)*2
							else: ## if p_weight >= rc_weight > lc_weight then stop and return root
								balanced = True
								return root
				else: ### last case => parent > min(child) thus swap with min of children
					if self.heap[(vpos+1)*2-1][0] < self.heap[(vpos+1)*2][0]: ## if lc<rc swap par with lc
						self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
						vpos = (vpos+1)*2-1
					elif self.heap[(vpos+1)*2-1][0] > self.heap[(vpos+1)*2][0]: ## if lc>rc swap par with rc
						self.heap[vpos], self.heap[(vpos+1)*2] = self.heap[(vpos+1)*2], self.heap[vpos]
						vpos = (vpos+1)*2
					else: ## if lc=rc then check weights to identify min of children
						if self.heap[(vpos+1)*2-1][1] >= self.heap[(vpos+1)*2][1]: ## if lc_weight>=rc_weight swap par with lc
							self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
							vpos = (vpos+1)*2-1
						else: ## if rc_weight>=lc_weight swap par with rc
							self.heap[vpos], self.heap[(vpos+1)*2] = self.heap[(vpos+1)*2], self.heap[vpos]
							vpos = (vpos+1)*2
					
	def remove(self, vpos):
		if vpos > len(self.heap)-1 or vpos < 0:
			raise Exception(vpos," is out of heap index range!")

		else:

			self.heap[vpos] = self.heap[-1]
			del self.heap[-1]
			balanced = False

			while not balanced:
				if (vpos+1)*2 -1 >= len(self.heap): ### if the unbalanced node is at the bottom of the tree then stop
					balanced =True

				elif (vpos+1)*2 -1 == len(self.heap)-1: ### if the unbalanced node has only one child (necessarily the left) check it
					if self.heap[vpos][0] < self.heap[(vpos+1)*2-1][0]: ### if the parent < child then stop 
						balanced = True
						
					elif self.heap[vpos][0] > self.heap[(vpos+1)*2-1][0] or self.heap[vpos][1] < self.heap[(vpos+1)*2-1][1]: ### if parent> child or (p=c and p_weight<p_child) then swap 
						self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
						vpos = (vpos+1)*2-1
					else: ### last case p=c and p_weight > p_child => stop and return root
						balanced = True

				else: ### parent has 2 children and we will swap with smallest child if necessary
					if self.heap[vpos][0] < min(self.heap[(vpos+1)*2-1][0], self.heap[(vpos+1)*2][0]): ## if parent < both children then stop and return root
						balanced = True
						
					elif self.heap[vpos][0] == min(self.heap[(vpos+1)*2-1][0], self.heap[(vpos+1)*2][0]): ## if parent == min(children) find min and compare
						if self.heap[(vpos+1)*2-1][0] < self.heap[(vpos+1)*2][0]: ## if parent = lchild < rchild 
							if self.heap[vpos][1] < self.heap[(vpos+1)*2-1][1]: ### if p_weight < lc_weight swap
								self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
								vpos = (vpos+1)*2-1
							else: ### par=lchild < rchild and p_weight >= lc_weight thus stop and return root
								balanced = True
								
						elif self.heap[(vpos+1)*2-1][0] < self.heap[(vpos+1)*2][0]: ## if parent = rchild < lchild 
							if self.heap[vpos][1] < self.heap[(vpos+1)*2-1][1]: ### if p_weight < rc_weight swap
								self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
								vpos = (vpos+1)*2-1
							else: ### par=rchild < lchild and p_weight >= rc_weight thus stop and return root
								balanced = True
								
						else: ### children are the same so check weights
							if self.heap[(vpos+1)*2-1][1] >= self.heap[(vpos+1)*2][1]: ### if lc_weight > rc_weight then check lc
								if self.heap[vpos][1] < self.heap[(vpos+1)*2-1][1]: ### if p_weight < lc_weight then swap
									self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
									vpos = (vpos+1)*2-1
								else: ## if p_weight >= lc_weight >= rc_weight then stop and return root
									balanced = True
									
							else:
								if self.heap[vpos][1] < self.heap[(vpos+1)*2][1]: ### if p_weight < rc_weight then swap
									self.heap[vpos], self.heap[(vpos+1)*2] = self.heap[(vpos+1)*2], self.heap[vpos]
									vpos = (vpos+1)*2
								else: ## if p_weight >= rc_weight > lc_weight then stop and return root
									balanced = True
									
					else: ### last case == parent > min(child) thus swap with min of children
						if self.heap[(vpos+1)*2-1][0] < self.heap[(vpos+1)*2][0]: ## if lc<rc swap par with lc
							self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
							vpos = (vpos+1)*2-1
						elif self.heap[(vpos+1)*2-1][0] > self.heap[(vpos+1)*2][0]: ## if lc>rc swap par with rc
							self.heap[vpos], self.heap[(vpos+1)*2] = self.heap[(vpos+1)*2], self.heap[vpos]
							vpos = (vpos+1)*2
						else: ## if lc=rc then check weights to identify min of children
							if self.heap[(vpos+1)*2-1][1] >= self.heap[(vpos+1)*2][1]: ## if lc_weight>=rc_weight swap par with lc
								self.heap[vpos], self.heap[(vpos+1)*2-1] = self.heap[(vpos+1)*2-1], self.heap[vpos]
								vpos = (vpos+1)*2-1
							else: ## if rc_weight>=lc_weight swap par with rc
								self.heap[vpos], self.heap[(vpos+1)*2] = self.heap[(vpos+1)*2], self.heap[vpos]
								vpos = (vpos+1)*2


class Med_Tracker:
	"""keeps track of median of array using a two heap approach"""
	def __init__(self):
		self.median = None
		self._LH = C_Heap([])
		self._RH = C_Heap([])

	def insert(self,n):
		if self.median == None:
			self.median = n
		else:
			if self._LH.len() == self._RH.len():
				if self.median <= n:
					self._RH.insert((n,0))
				else:
					self._RH.insert((self.median,0))
					if self._LH.len() > 0:
						if n >= -self._LH.self(0)[0]:
							self.median = n
						else:
							self.median = -self._LH.pop()[0]
							self._LH.insert((-n,0))
					else:
						self.median = n
			else:
				if self.median < n:
					self._LH.insert((-self.median,0))
					if n <= self._RH.self(0)[0]:
						self.median = n
					else:
						self.median = self._RH.pop()[0]
						self._RH.insert((n,0))
				else:
					self._LH.insert((-n,0))

	def get_med(self):
		return self.median

# def Gather_Graph_List_W(fname):
# 	# """Specific for reading in file from Stanford Class"""
# 	Edges = []
# 	Nodes = []
# 	Weights = []
# 	ECounter = -1
# 	Nodedict = dict()
# 	NodeSet = set()
# 	with open(fname) as f:
# 		for line in f.readlines():
# 			line = line.split()
# 			if len(line) > 2:
# 				ECounter += 2
# 				Weights.append(int(line[2]))
# 				Weights.append(int(line[2]))
# 				line1 = [int(line[0])-1,int(line[1])-1]
# 				line2 = [int(line[1])-1,int(line[0])-1]
# 				Edges.append(line1)
# 				Edges.append(line2)
# 				if line1[0] not in NodeSet:
# 					NodeSet.add(line1[0])
# 					Nodedict[line1[0]] = [[ECounter-1],[ECounter]] 
# 				else:
# 					Nodedict[line1[0]][0].append(ECounter-1)
# 					Nodedict[line1[0]][1].append(ECounter)

# 				if line1[1] not in NodeSet:
# 					NodeSet.add(line1[1])
# 					Nodedict[line1[1]] = [[ECounter],[ECounter-1]] 
# 				else:
# 					Nodedict[line1[1]][0].append(ECounter)
# 					Nodedict[line1[1]][1].append(ECounter-1)

# 	numnodes = len(NodeSet)
# 	for i in range(numnodes):
# 		Nodes.append(Nodedict[i])

# 	return Nodes, Edges, Weights

##### Tests
# if __name__=='__main__':

	# newlist = [(5,-1),(1,3),(6,4),(3,6),(7,2),(8,8),(9,4),(4,0),(5,-2),(4,-3),(8,7)]
	# for i in newlist:
	# 	newmedtrack.insert(i)
	# 	meds.append(newmedtrack.get_med())
	
	# print(meds)

	# nh = C_Heap([])

	# for i in newlist:
	# 	nh.insert(i)

	# nh.remove(nh.index((5,0)))

	# print("Cust Heap print")
	# for i in range(len(nh.self())):
	# 	print(nh.pop())
	
