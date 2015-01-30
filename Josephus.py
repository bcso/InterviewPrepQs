## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

#

# Josephus

# Input: Number of players
# Output: Index (1-based) of the winner

#Define a Node
class ListNode:
    def __init__(self, item, next):
        self.item = item
        self.next = None

#Create CLL
class CircularlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #Print the current linked list object
    def __str__(self):
        finalStr = ""
        currNode = self.head

        #Iterate through the current list for the size value
        for x in xrange(self.size):
            finalStr = finalStr + str(currNode.item) + " "
            currNode = currNode.next

        return finalStr

    #Load the current list of players
    #INPUT: inputPlayers -> list input of players
    #       pNum         -> length of list of players
    def loadPlayers(self, inputPlayers, pNum):
        if type(pNum) != type(0):
            raise TypeError, "pNum must be of type integer!"
        if type(inputPlayers) != type([1]):
            raise TypeError, "inputPlayers must be of type List!"
        if len(inputPlayers) != pNum:
            raise ValueError, "pNum must be equal to the length of inputPlayers"

        for x in xrange(pNum):
            #Create new node with next value in list
            newNode = ListNode(inputPlayers[x], None)

            #First node creation case
            if self.head == None:
                self.head = newNode
                self.tail = newNode
                self.tail.next = self.head
                self.size += 1
            #Nodes created beyond first node case
            else:
                self.tail.next = newNode
                self.tail = self.tail.next
                self.tail.next = self.head
                self.size += 1

    #Find the winner
    #OUTPUT: String value of player
    def findWinner(self):
        if self.size == 0:
            raise ValueError, "There must be at least one player!"

        currNode = self.head #Start off the search with 0th player

        while self.size != 1: #Iterate until one player remains
            currNode.next = currNode.next.next #Delete every other player
            currNode = currNode.next #Move current pointer
            self.size = self.size - 1

        return str(currNode.item)


if __name__ == '__main__':
    inputPlayers = [1,2,3,4,5,6]

    cllOfPlayers = CircularlyLinkedList()
    cllOfPlayers.loadPlayers(inputPlayers, len(inputPlayers))

    print "This is the current list of players: " + str(cllOfPlayers) #Show players
    print "The winner is player.... " + cllOfPlayers.findWinner() + " !"
