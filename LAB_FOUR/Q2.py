class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def addNode(self, info):
        newNode = Node(info)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def deleteNode(self, info):
        if self.head == None:
            return
        if self.head.info == info:
            self.head = self.head.next
            return
        current = self.head
        while current.next != None:
            if current.next.info == info:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current != None:
            print(current.info, end=' ')
            current = current.next

linkList = LL()
linkList.addNode(212)
linkList.addNode(145)
linkList.addNode(467)
linkList.addNode(535)
linkList.addNode(349)
linkList.addNode(767)
linkList.addNode(926)
print("Printing The Linked List \n")
linkList.display()
print("\n")
linkList.deleteNode(212)
linkList.deleteNode(767)
print("Printing The Linked List After Removing 212 And 767 From List \n")
linkList.display()
