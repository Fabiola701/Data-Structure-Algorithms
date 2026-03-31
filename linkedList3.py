class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        temp1 = self.head
        while temp1:
            print(temp1.data, end=" -> ")
            temp1 = temp1.next
        print("None")

#namaObject = namaClass(argument)
node1 = Node("Andi")
node2 = Node("Jessica")
node3 = Node("Andi")

l1 = LinkedList()
l1.head = node1
node1.next = node2
node2.next = node3

linkedObject = LinkedList()
linkedObject.display()




