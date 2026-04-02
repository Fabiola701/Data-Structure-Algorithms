# file: linked_list_grades.py

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)

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


linkTugas = LinkedList()

# initialize list correctly
for grade in (100, 90, 75):
    linkTugas.append(grade)

while True:
    print("\n1. Add grade")
    print("2. Display all grades")
    print("3. Display grades with 100")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            data = int(input("Enter grade to add: "))
            linkTugas.append(data)
        except ValueError:
            print("Grade must be an integer.")

    elif choice == 2:
        linkTugas.display()

    elif choice == 3:
        linkTugas.display100()

    elif choice == 4:
        break

    else:
        print("Invalid choice")