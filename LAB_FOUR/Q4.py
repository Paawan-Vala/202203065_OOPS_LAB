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

    def delete_greater_than(self, value):
        while self.head is not None and self.head.info > value:
            self.head = self.head.next
        if self.head is None:
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.info > value:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next


    def display(self):
        current = self.head
        while current != None:
            print(current.info, end=' ')
            current = current.next

linkList = LL()
while True:
    user_input = input("Enter a number between 1 and 50 (press Enter to stop): ")
    if user_input == "":
        break
    number = int(user_input)
    if 1 <= number <= 50:
        linkList.addNode(number)
    else:
        print("Invalid input! Enter a number between 1 and 50.")
linkList.delete_greater_than(25)
print("It Prints The New List")
linkList.display()