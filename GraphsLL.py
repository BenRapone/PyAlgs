import resource
import sys
import heapq as hq
import time
orig_stdout = sys.stdout


# # Will segfault without this line with large lists.
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

class Nt_Graph_LL:
	"""Net Work Graph Class with methods for BFS, DFS based operations and more"""
	def __init__(self,vl,el, ew=-1): ## initialize graph with vtx list, edge list, edge weight list (linked list format)
		self.vertnum = len(vl)
		self.edgenum = len(el)
		self.vheap = []
		self.mst = []
		self.mst_cost = 0
		self.heapkey = {}
		self.v2e = vl
		self.e2v = el
		self.ew = ew
		self.vatt = dict() ## first touched status, second touched status, topolabel, SCC label
		self.topolabel = -1
		self.SCCcount = 0
		self.SCC = dict()
		self.touched = set()
		self.components = []
		self.BFS = dict()
		self.Level = dict()
		self.ShortPathList_D = dict()
		self.SCCq = [0]*self.vertnum
		for i in range(self.vertnum):  ## 
			self.vatt[i] = [False, False, -1, -1]  

	def get_topolabel(self): 
		"""retrieve topological ordering in list form"""
		return [(i+1, self.vatt[i][2]+1) for i in range(self.vertnum)]

	def get_SCC(self):
		"""retrieve dictionary of Securely Connected Components"""
		return self.SCC 

	def get_SCCpop(self,k=-1): ## retrieve the top k largest SCCs
		if k == -1:
			k = len(self.SCC)
		SCCpoplist = [len(self.SCC[i]) for i in list(self.SCC.keys())]
		SCCpoplist.sort(reverse = True)
		if k > len(self.SCC):
			return SCCpoplist
		else:
			return SCCpoplist[:k]

	def addEdge(self,u,v): ## 
		self.e2v.append([u,v])
		self.edgenum += 1
		self.v2e[u][0].append(self.edgenum)
		self.v2e[v][1].append(self.edgenum)

	def DFS_rec(self, v, tr, rev = 0, top =False, scc = False):
		""" input is a vertex you wish to start from (v), touch round (0 or 1) and whether you wish to reverse the graph edges (default is no 0)
		output is all nodes that can be reached from initial v"""
		self.vatt[v][tr] = True
		self.touched.add(v)
		for edge in self.v2e[v][rev]:
			w = self.e2v[edge][1-rev]
			if not self.vatt[w][tr]:
				self.DFS_rec(w,tr,rev,top,scc)
	
		if top:
			self.vatt[v][2] = self.topolabel
			self.SCCq[self.topolabel] = v
			self.topolabel += -1

		if scc:
			self.SCC[self.SCCcount].append(v)
			self.vatt[v][3] = self.SCCcount

	def DFS_Topo(self,tr=0,rev=0):
	    """ find a topological ordering using first or second pass (tr is 0 or 1) and in rev order (default false)"""
	    self.touched = set()
	    self.topolabel = self.vertnum-1
	    for node in range(self.vertnum):
	        if not self.vatt[node][tr]:
	            self.DFS_rec(node,tr,rev,True)

	def DFS_SCC(self):
		""" given a directed graph in linked list form, find the SCCs returns SCCs and count of SCCs"""

		self.DFS_Topo(0,1)
		self.touched = set()
		self.SCCcount = 0

		for node in self.SCCq:
			if not self.vatt[node][1]:
				self.SCCcount += 1
				self.SCC[self.SCCcount] = []
				self.DFS_rec(node,1,0,False,True)

	def UCCBFS(self): 
		""" input is a undirected graph (Nodes, Edges) in linked list form
		output is the number of connected components and a list containing them"""
		nodeset = set(range(self.vertnum))
		while len(nodeset) > 0:
			v = nodeset.pop()
			q = [v]
			touched = set([v])
			while len(q) > 0:
				vtx = q.pop(0)
				for edge in self.v2e[vtx][0]:
					w = self.e2v[edge][1]
					if w not in touched:
						touched.add(w)
						q.append(w)
						nodeset.remove(w)
				self.components.append(touched)

	def get_UCCBFS(self):
		""" Gather UCCBFS """
		return len(self.components), self.components

	def BFSCalc(self,v): 
		""" input is a directed graph (Nodes, Edges) in linked list form and a vertex you wish to start from
		output is all nodes that can be reached from v and number of levels out from v"""
		self.BFS[v] = set([v])
		q = [v]
		levelcount = 0
		levelnode = v
		while len(q) > 0:
			vtx = q.pop(0)
			for edge in self.v2e[vtx][0]:
				w = self.e2v[edge][1]
				if w not in self.BFS[v]:
					self.BFS[v].add(w)
					q.append(w)
			if vtx == levelnode:
				levelcount += 1
				levelnode = w
		self.BFS[v] = (self.BFS[v],levelcount)

	def get_BFS(self,v):
		if v in self.BFS:
			return self.BFS[v]
		else:
			return -1

	def ShortestPath_BFS(self,v,s): 
		""" input is a directed graph (Nodes, Edges) in linked list form and a vertex, v, you wish to start from and end at s
		output is the shortest number of levels from v to s, i.e. smallest number of edges between or -1 if not connected"""
		touched = set([v])
		q = [v]
		levelcount = 0
		levelnode = v
		while len(q) > 0:
			vtx = q.pop(0)
			for edge in self.v2e[vtx][0]:
				w = self.e2v[edge][1]
				if w not in touched:
					if w == s:
						return levelcount+1
					touched.add(w)
					q.append(w)
			if vtx == levelnode:
				levelcount += 1
				levelnode = w
		return -1

	def ShortestPath_Dijkstra_Heap(self,v):
		"""Calculates the shortest path list to all other vertices from vertex v in network of positive weighted edges """
		if self.ew == -1:
			self.ew = [1]*self.edgenum
		self.ShortPathList_D[v] = dict()
		self.ShortPathList_D[v][v] = 0
		self.heapkey = {}
		self.vheap = []
		nodeset = set(range(self.vertnum))
		nodeset.remove(v)
		touchable = set()
		maxvtxd = v
		for edge in self.v2e[v][0]:  ### look through all outgoing edges and add them to heap
			hq.heappush(self.vheap, (self.ew[edge],self.e2v[edge][1]))
			self.heapkey[self.e2v[edge][1]] = (self.ew[edge],self.e2v[edge][1])
			touchable.add(self.e2v[edge][1])

		while self.vheap:
			key = self.vheap_pop()
			if key == -1:
				break
			self.ShortPathList_D[v][key[1]] = key[0]
			nodeset.remove(key[1]) 
			touchable.remove(key[1])

			for edge in self.v2e[key[1]][0]:  #### look through all outgoing edges and add them to heap
				if self.e2v[edge][1] in nodeset:  #### Only consider edges to vtxs that have not yet been found
					if self.e2v[edge][1] not in touchable:  #### if not yet touchable then found path to heap
						hq.heappush(self.vheap, (key[0]+self.ew[edge], self.e2v[edge][1]))
						self.heapkey[self.e2v[edge][1]] = (key[0]+self.ew[edge], self.e2v[edge][1])
						touchable.add(self.e2v[edge][1])

					else:
						if key[0]+self.ew[edge] < self.heapkey[self.e2v[edge][1]][0]: ### if touchable compare found path to previous min path
							hq.heappush(self.vheap, (key[0]+self.ew[edge], self.e2v[edge][1]))
							self.heapkey[self.e2v[edge][1]] = (key[0]+self.ew[edge], self.e2v[edge][1])

	def Mst_Prim_Heap(self,v):
		"""Calculates the minimum spanning tree starting with vertex v with heap method using python heapq"""
		if self.ew == -1:
			self.ew = [1]*self.edgenum

		self.mst_cost = 0
		self.vheap = []
		nodeset = set(range(self.vertnum))
		nodeset.remove(v)
		touchable = set()
		maxvtxd = v
		for edge in self.v2e[v][0]:  ### look through all outgoing edges and add them to heap
			hq.heappush(self.vheap, (self.ew[edge],self.e2v[edge][1],edge))
			touchable.add(self.e2v[edge][1])

		while nodeset:
			key = hq.heappop(self.vheap)
			if key == -1:
				break

			if key[1] in touchable:
				self.mst.append(key[2])
				self.mst_cost = self.mst_cost + key[0]
				nodeset.remove(key[1]) 
				touchable.remove(key[1])

				for edge in self.v2e[key[1]][0]:  #### look through all outgoing edges and add them to heap
					if self.e2v[edge][1] in nodeset:  #### Only consider edges to vtxs that have not yet been found
						hq.heappush(self.vheap, (self.ew[edge], self.e2v[edge][1], edge))
						touchable.add(self.e2v[edge][1])


	def get_mst_cost(self):
		return self.mst_cost

	def ShortestPath_Dijkstra(self,v):
		"""Calculates the shortest path list to all other vertices from vertex v in network of positive weighted edges """
		if self.ew == -1:
			self.ew = [1]*self.edgenum
		CapW = sum(self.ew)+1
		nodeset = set(range(self.vertnum))
		self.ShortPathList_D[v] = dict()
		self.ShortPathList_D[v][v] = 0
		nodeset.remove(v)
		maxvtxd = v
		while nodeset:
			maxl = CapW
			oldmaxvtx = maxvtxd
			for vtx in self.ShortPathList_D[v].keys():
				for edge in self.v2e[vtx][0]:
					if self.ShortPathList_D[v][vtx]+self.ew[edge] < maxl and self.e2v[edge][1] in nodeset:
						maxl = self.ShortPathList_D[v][vtx]+self.ew[edge]
						maxvtxo = vtx
						maxvtxd = self.e2v[edge][1]
			if oldmaxvtx == maxvtxd:
				break
			nodeset.remove(maxvtxd)
			self.ShortPathList_D[v][maxvtxd] = maxl

	def get_ShortestPath_Dijkstra(self,v,s):
		""" Return shortest path from v to s """
		if v in self.ShortPathList_D.keys():
			if s in self.ShortPathList_D[v].keys():
				return self.ShortPathList_D[v][s]
		return -1
