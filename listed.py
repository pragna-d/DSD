class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def isListempty(self):
        if self.head is None:
            return True
        else:
            return False
    def listLength(self):
        currentNode=self.head
        length =0
        while currentNode is not None:
            length +=1
            currentNode=currentNode.next
        return length
    def insertHead(self,newnode):
        # data => matthew, next => none
        temporaryNode=self.head
        self.head=newnode
        self.head.next=temporaryNode
        del temporaryNode
    def insertAt(self,newnode,position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if position == 0:
            self.insertHead(newnode)
            return
        currentNode=self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next=newnode
                newnode.next=currentNode
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition += 1
    def insertEnd(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
        
    def deleteHead(self):
        if self.isListempty() is False:
            previosHead=self.head
            self.head=self.head.next
            previosHead.next=None
        else:
            print("Linked list is empty . delete failed")
    def deleteAt(self,position):
        if position < 0 or position >= self.listLength():
            print("Invalid position")
            return
        if self.isListempty()is false:
            if position == 0:
                self.deleteHead()
                return
            currentNode=self.head
            currentPosition=0
            while True:
                if currentPosition==position:
                    previousNode.next=currentNode.next
                    currentNode.next=None
                    break
                previousNode=currentNode
                currentNode=currentNode.next
                currentPosition +=1
        # else:
            # print("list is empty")
           
    def deleteEnd(self):
        if self.isListempty()is False:
            if self.head.next is None:
                self.deleteHead()
                return
            lastnode=self.head
            while lastnode.next is not None:
                previousNode=lastnode
                lastnode=lastnode.next
            previousNode.next=None
        else:
            print("linkedlist is empty . delete failed ")
                
    def printlist(self):
        if self.head is None:
            print("list is empty")
            return
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
firstnode =node("John")
linkedList=LinkedList()
linkedList.insertEnd(firstnode)
secondnode=node("Ben")
linkedList.insertEnd(secondnode)
# thirdNode=Node("mathew")
# linkedList.insertHead(thirdNode)
thirdnode=node("Mathew")
linkedList.insertEnd(thirdnode)
# linkedList.daleteEnd()
linkedList.deleteAt(0)
linkedList.printList()
# firstnode=node("pragna")
# linkedList=LinkedList()
# linkedList.deleteEnd(firstnode)

# secondnode=node("sam")
# # linkedList=LinkedList()
# # linkedList.deleteEnd(secondnode)

# thirdnode=node("matthew")
# # linkedList=LinkedList()
# # linkedList.deleteEnd(thirdnode)
# linkedList.deleteAt(1)
# linkedList.printlist()