class twoStackQueue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enqueue(self, items):
		for item in items:
			self.s1.append(items.pop());

	def dequeue(self):
		if len(self.s2) > 0:
			return self.s2.pop()
		else:
			while len(self.s1) > 0:
				self.s2.append(self.s1.pop())
		return self.s2.pop()

	def __str__(self):
		return "s1: " + str(self.s1) + " s2: " + str(self.s2)


q = twoStackQueue()
items = [1,2,3,4]
q.enqueue(items)
print str(q)
print q.dequeue()
print str(q)