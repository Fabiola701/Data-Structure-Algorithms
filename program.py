class Node:
    def __init__ (self, data, prioritas):
        self.data = data
        self.prioritas = prioritas
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
    
    def append(self, data,prioritas):
        new_node = Node(data,prioritas)
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
    
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

linkTugas = LinkedList()
while True:
    print("1. Add")
    print("2. Display")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter data to add: ")
        prioritas = input("Enter prioritas: ")
        linkTugas.append(data, prioritas)
    elif choice == 2:
        linkTugas.display()
    elif choice == 3:
        break
    else:
        print("Invalid choice")

# n1 = Node(10)
# n2 = Node(15)
# n1.next = n2
# ll = LinkedList()
# ll.head = n1
# print(ll.head.data)        # Output: 10
# print(ll.head.next.data)   # Output: 15
# This code defines a Node class and a LinkedList class.
# It creates two nodes and links them together in a linked list.

# linkTugas = LinkedList()
# linkTugas.append(5)
# linkTugas.append(10)
# linkTugas.append(15)
# linkTugas.append(20)

# linkTugas.display()  # Output: 5 -> 10 -> 15 -> 20 -> None# This code creates a linked list using the LinkedList class,
# appends several nodes to it, and displays the entire list.# demonstrating the functionality of the linked list implementation.