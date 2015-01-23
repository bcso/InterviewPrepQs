from collections import deque

class Node:
	def __init__(self):
		self.visited = False
		self.value = None
		self.children = []

def bfs(node):
	q = deque()
	node.visited = True
	q.append(node)
	while len(q) > 0:
		newNode = q.popleft()
		for childNode in newNode.children:
			if childNode.visited == False:
				childNode.visited = True
				q.append(childNode)



