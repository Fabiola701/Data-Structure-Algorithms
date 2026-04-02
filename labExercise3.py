class Node:
    def __init__ (self, nama, jurusan, nilai):
        self.nama = nama
        self.jurusan = jurusan
        self.nilai = nilai
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
    
    def append(self, nama, jurusan, nilai):
        new_node = Node(nama, jurusan, nilai)
        if not self.head:
            self.head = new_node
            return
        
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node
    
    def append_beginning(self, nama, jurusan, nilai):
        new_node = Node(nama, jurusan, nilai)
        new_node.next = self.head
        self.head = new_node
    
    def find(self, nilai):
        temp = self.head
        while temp:
            if temp.nilai == nilai:
                print(f"Found: {temp.nama}, {temp.jurusan}, {temp.nilai}")
            temp = temp.next
        print("Data not found.")
    
    def displayAll(self):
        temp = self.head
        while temp:
            print(f"{temp.nama}, {temp.jurusan}, {temp.nilai}")
            temp = temp.next

    def displaySI(self):
        temp = self.head
        count = 0
        while temp:
            if temp.jurusan == "SI":
                print(f"{temp.nama}, {temp.jurusan}, {temp.nilai}")
                count += 1
            temp = temp.next
        print(f"Total students in SI: {count}")

    def displayTI(self):
        temp = self.head
        count = 0
        while temp:
            if temp.jurusan == "TI":
                print(f"{temp.nama}, {temp.jurusan}, {temp.nilai}")
                count += 1
            temp = temp.next
        print(f"Total students in TI: {count}")
    def remove(self, key):
        if self.head is None:
            return
        if self.head.nama == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.nama == key:
                current.next = current.next.next
                return
            current = current.next

linkMahasiswa = LinkedList()
while True:
    print("1. Add data at the end")
    print("2. Add data at the beginning")
    print("3. Display all data")
    print("4. Find data based on nilai")
    print("5. Display all data based on jurusan SI and total number of students")
    print("6. Display all data based on jurusan TI and total number of students")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        nama = input("Enter nama: ")
        jurusan = input("Enter jurusan(SI/TI): ")
        nilai = input("Enter nilai: ")
        linkMahasiswa.append(nama, jurusan, nilai)
    elif choice == 2:
        nama = input("Enter nama: ")
        jurusan = input("Enter jurusan(SI/TI): ")
        nilai = input("Enter nilai: ")
        linkMahasiswa.append_beginning(nama, jurusan, nilai)
    elif choice == 3:
        linkMahasiswa.displayAll()
    elif choice == 4:
        nilai = input("Enter nilai to find: ")
        linkMahasiswa.find(nilai)
    elif choice == 5:
        linkMahasiswa.displaySI()
    elif choice == 6:
        linkMahasiswa.displayTI()
    elif choice == 7:
        break
    else:
        print("Invalid choice")

