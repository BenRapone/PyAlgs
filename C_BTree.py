class C_BTree:
	"""Class for a custum binarary search tree stored as a dictionary with manual rebalance option"""
	def __init__(self,l=[]): ## Left Small, Right Big
		self.btree = dict()
		if l != []:
			if len(l) == 1:
				self.btree[l[0]] = [-1,-1,-1] ## value, LftChild, RgtChild, Parent
				self.root = l[0]

			else:
				l.sort()	### If list is non-empty sort first and take advantage of structure to create balanced initial tree
				for i in range(len(l)):
					self.btree[l[i]]= [-1,-1,-1]
				llist = l[0:len(l)//2]
				rlist = l[len(l)//2+1:]
				self.root = l[len(l)//2]
				self.find_parchild(llist,rlist,l[len(l)//2])
		self.slist = l

	def self(self,v=-1):
		if v == -1:
			return self.btree.keys()
		else:
			return self.btree[v]

	def find_parchild(self,ll,rl,p):
		if len(ll)>0:
			self.btree[p][0] = ll[len(ll)//2]  ## set child loc
			self.btree[ll[len(ll)//2]][2] = p ### set parent loc
			if len(ll) > 1:
				self.find_parchild(ll[0:len(ll)//2],ll[len(ll)//2+1:],ll[len(ll)//2])   ## set child of child loc

		if len(rl)>0:
			self.btree[p][1] = rl[len(rl)//2] ## set child loc
			self.btree[rl[len(rl)//2]][2] = p ### set parent loc
			if len(rl) > 1:
				self.find_parchild(rl[0:len(rl)//2],rl[len(rl)//2+1:],rl[len(rl)//2])

	def sort(self,cnode=0,init=True):
		if init==True:
			self.slist = []
			cnode = self.root

		if self.btree[cnode][0] == -1:
			self.slist.append(cnode)

		elif self.btree[cnode][0] != -1:
			self.sort(self.btree[cnode][0],False)

		if self.btree[cnode][0] != -1 or self.btree[cnode][1] != -1:
			self.slist.append(cnode)

		if self.btree[cnode][1] != -1:
			self.sort(self.btree[cnode][1],False)

	def get_sort(self):
		return self.slist

	def delete(self,v):
		if self.btree[v][0] == -1 and self.btree[v][1] == -1:
			if v != self.root:
				if self.btree[self.btree[v][2]][0] == v:
					self.btree[self.btree[v][2]][0] = -1
				else:
					self.btree[self.btree[v][2]][1] = -1
			else:
				self.root = -1

		elif self.btree[v][0] == -1:
			if v != self.root:
				self.btree[self.btree[v][1]][2] = self.btree[v][2] 
				if self.btree[self.btree[v][2]][0] == v:
					self.btree[self.btree[v][2]][0] = self.btree[v][1]
				else:
					self.btree[self.btree[v][2]][1] = self.btree[v][1]
			else:
				self.root = self.btree[v][1]

		elif self.btree[v][1] == -1:
			if v != self.root:
				self.btree[self.btree[v][0]][2] = self.btree[v][2] 
				if self.btree[self.btree[v][2]][0] == v:
					self.btree[self.btree[v][2]][0] = self.btree[v][0]
				else:
					self.btree[self.btree[v][2]][1] = self.btree[v][0]
			else:
				self.root = self.btree[v][0]

		else:
			lc = self.btree[v][0]
			balance = True
			while balance:
				if self.btree[lc][1] != -1:
					lc = self.btree[lc][1]
				else:
					balance = False

			if lc == self.btree[v][0]:
				if v != self.root:
					self.btree[self.btree[v][0]][2] = self.btree[v][2] 
					if self.btree[self.btree[v][2]][0] == v:
						self.btree[self.btree[v][2]][0] = self.btree[v][0]
					else:
						self.btree[self.btree[v][2]][1] = self.btree[v][0]
				else:
					self.root = self.btree[v][0]
					self.btree[lc][2] = -1 


			else:
				if self.btree[lc][0] != -1:
					self.btree[self.btree[lc][0]][2] = self.btree[lc][2] 
					if self.btree[self.btree[lc][2]][0] == lc:
						self.btree[self.btree[lc][2]][0] = self.btree[lc][0]
					else:
						self.btree[self.btree[lc][2]][1] = self.btree[lc][0]


				if v != self.root:
					self.btree[lc][2] = self.btree[v][2]
					if self.btree[self.btree[v][2]][0] == v:
						self.btree[self.btree[v][2]][0] = lc
					else:
						self.btree[self.btree[v][2]][1] = lc

				else:
					self.root = lc
					self.btree[lc][2] = -1

				self.btree[lc][0] = self.btree[v][0]
				self.btree[self.btree[v][0]][2] = lc
			
			self.btree[lc][1] = self.btree[v][1]
			self.btree[self.btree[v][1]][2] = lc

		del self.btree[v]

















		

