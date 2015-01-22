class ListNode:
	def __init__(self, item, next):
		self.item = item
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def append(self, item):
		if self.head == None:
			node = ListNode(item, None)
			self.head = node
			self.tail = node
		else :
			node = ListNode(item, None)
			self.tail.next = node
			self.tail = self.tail.next
			self.size += 1

	def __str__(self):
		currNode = self.head
		ListString = ""
		while currNode.next != None:
			ListString = ListString + str(currNode.item) + ", "
			currNode = currNode.next
		ListString = ListString + str(currNode.item)
		return ListString

	def getHead(self):
		return self.head

	def getTail(self):
		return self.tail