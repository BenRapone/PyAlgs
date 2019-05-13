import resource
import sys
orig_stdout = sys.stdout


# # Will segfault without this line.
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)



class Nt_Graph:
	"""Class of Network graphs in linked list form with built-in DFS algs"""
	def __init__(self,vl,el): ## initialize graph with vtx list, edge list (linked list format)
		self.vertnum = len(vl)
		self.edgenum = len(el)
		self.v2e = vl
		self.e2v = el
		self.vatt = dict() ## first touched status, second touched status, topolabel, SCC label
		self.topolabel = -1
		self.SCCcount = 0
		self.SCC = dict()
		self.touched = set()
		self.SCCq = [0]*self.vertnum
		for i in range(self.vertnum):  ## 
			self.vatt[i] = [False, False, -1, -1]  

	def get_topolabel(self): ##retrieve topological ordering in list form
		return [(i+1, self.vatt[i][2]+1) for i in range(self.vertnum)]

	def get_SCC(self): ## retrieve dictionary of Securely Connected Components
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


