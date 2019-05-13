class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass

class C_Stack:
	"""LIFO Stack implementation using linked lists"""
	class _Node:
		"""Subclass for node information"""
		__slots__='_element','_next'
		def __init__(self,element,next):
			self._element = element
			self._next = next

	def __init__(self):
		"""Create empty Stack"""
		self._head = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def push(self,n):
		self._head = self._Node(n,self._head)
		self._size += 1

	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._head._element

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		answer = self._head._element
		self._head = self._head._next
		self._size -=1
		return answer

class C_Que:
	"""FIFO queue imp using linked lists with dynamic capicity"""
	DEFAULT_CAPACITY = 10

	def __init__(self):
		"""Init empty queue"""
		self._data = [None]*C_Que.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		"""Return (but do not remove) the element at the front """
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		"""Pop first element of queue"""
		if self.is_empty():
			raise Empty('Queue is empty')
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front+1) % len(self._data)
		self._size -= 1
		return answer

	def enqueue(self, n):
		if self._size == len(self._data):
			self._resize(2*len(self))
		avail = (self._front+self._size) % len(self._data)
		self._data[avail] = n
		self._size +=1

	def _resize(self,cap):
		old = self._data
		self._data = [None]*cap
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1+walk) % len(old)
		self._front = 0
