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
    def search(self, info):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.info == info:
                return index
            current_node = current_node.next
            index += 1
        return -1

linkList = LL()
linkList.addNode(1)
linkList.addNode(5)
linkList.addNode(7)
linkList.addNode(3)
linkList.addNode(8)
linkList.addNode(2)
linkList.addNode(3)
index = linkList.search(7)
if index != -1:
    print(f"The index of 7 is: {index}")
else:
    print("7 not found in the list")
