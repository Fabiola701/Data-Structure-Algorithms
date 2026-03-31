# file: linked_list_priority.py

class Node:
    def __init__(self, data, prioritas):
        self.data = data
        self.prioritas = prioritas
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data, prioritas):
        new_node = Node(data, prioritas)

        if self.head is None:
            self.head = new_node
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        ptr.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(f"[{temp.data}, {temp.prioritas}]", end=" -> ")
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
    print("\n1. Add")
    print("2. Display")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input")
        continue

    if choice == 1:
        data = input("Enter data to add: ")
        prioritas = input("Enter prioritas (high/medium/low): ")
        linkTugas.append(data, prioritas)

    elif choice == 2:
        linkTugas.display()

    elif choice == 3:
        break

    else:
        print("Invalid choice")