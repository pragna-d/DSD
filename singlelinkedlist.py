class Node:
    def _init_(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def _init_(self):
        self.head=None

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def listLength(self):
       currentNode=self.head
       length=0
       while currentNode is not None:
           length+=1
           currentNode = currentNode.next
       return length

    def insertHead(self,newNode):
        # data => matthew,next=>None
        temporaryNode=self.head  #john
        self.head=newNode   #Matthew
        self.head.next=temporaryNode
        del temporaryNode

    def insertAt(self,newNode, position):
        # head=>10 =>20=>None // newNode=15=>None ||position=1
        if position<0 or position>self.listLength():
            print("Invalid position ")
            return 

        if position==0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition=0
        while True:
            if currentPosition == position:
                previousNode.next =newNode
                newNode.next=currentNode
                break
            previousNode = currentNode
            currentNode=currentNode.next
            currentPosition+=1

    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            # self.head.next=newNode
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next =newNode

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead=self.head
            self.head = self.head.next
            previousHead.next=None
        else:
            print("Linkedlist is empty. Delete failed")

    def deleteAt(self,position):
        if position<0 or position>=self.listLength():
            print("invalid position")
            return
        if self.isListEmpty() is False:
            if position==0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition=0
            while True:
                if currentPosition==position:
                    previousNode.next=currentNode.next
                    currentNode.next=None
                    break
                previousNode =currentNode
                currentNode = currentNode.next
                currentPosition += 1
    
    def daleteEnd(self):
        lastNode=self.head
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next
        previousNode.next = None



    def printList(self):
        # head => john => Ben =>Mathew =>None
        if self.head is None:
            print("List is empty")

        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    
        

   

# Node => data, next
# firstNode.data => john, firstNode.next = None
firstnode =Node("John")
linkedList=LinkedList()
linkedList.insertEnd(firstnode)
secondnode=Node("Ben")
linkedList.insertEnd(secondnode)
# thirdNode=Node("mathew")
# linkedList.insertHead(thirdNode)
thirdnode=Node("Mathew")
linkedList.insertEnd(thirdnode)
# linkedList.daleteEnd()
linkedList.deleteAt(0)
linkedList.printList()