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
    
    def display100(self):
        temp = self.head
        count = 0
        while temp:
            if temp.data == 100:
                count += 1
            temp = temp.next
        print(f"There are {count} grades with 100.")

n1 = Node(100)
n2 = Node(90)
n3 = Node(75)

n1.next = n2
n2.next = n3

linkTugas = LinkedList()
linkTugas.head = n1


while True:
    print("1. Add grade")
    print("2. Display all grades")
    print("3. Display grades with 100")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter grade to add: ")
        linkTugas.append(data)
    elif choice == 2:
        linkTugas.display()
    elif choice == 3:
        linkTugas.display100()
    elif choice == 4:
        break
    else:
        print("Invalid choice")

