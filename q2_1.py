from LinkedList import *

a = LinkedList()
#Create a normal list

a.append(2)
a.append('good')
a.append(2)
a.append('b')
a.append(True)
a.append(2)
a.append('b')
a.append(True)
a.append(2)
a.append('b')
a.append(True)
print str(a)

def removeDupes(inList):
	seen = []
	head = inList.getHead()
	tail = inList.getTail()
	currNode = head
	prevNode = None

	while currNode != None:
		if currNode.item in seen:
			prevNode.next = currNode.next
		else:
			seen.append(currNode.item)
			prevNode = currNode
		currNode = currNode.next


	print str(inList)

removeDupes(a)