class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    def remove(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next



n1 = Node(10)
n2 = Node(15)
n1.next = n2
ll = LinkedList()
ll.head = n1
print(ll.head.data)        # Output: 10
print(ll.head.next.data)   # Output: 15
# This code defines a Node class and a LinkedList class.
# It creates two nodes and links them together in a linked list.

linkObject = LinkedList()
linkObject.append(5)
linkObject.append(10)
linkObject.append(15)
linkObject.append(20)

linkObject.display()  # Output: 5 -> 10 -> 15 -> 20 -> None# This code creates a linked list using the LinkedList class,
# appends several nodes to it, and displays the entire list.# demonstrating the functionality of the linked list implementation.