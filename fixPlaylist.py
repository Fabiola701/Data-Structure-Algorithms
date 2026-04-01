# Program untuk mengelola playlist lagu menggunakan linked list

class Node:
    def __init__ (self, no, judulLagu):
        self.no = no
        self.judulLagu = judulLagu
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def add_song(self, no, judulLagu):
        new_node = Node(no, judulLagu)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    
    def deleteFirst(self):
        if self.head is None:
            print("Tidak ada yang dapat dihapus")
            return
        
        hapus = self.head.no
        self.head = self.head.next
        print(f"Lagu ke-{hapus} telah terhapus")
    
    def deleteLast(self):
        
        if self.head is None:
            print("Tidak ada yang dapat dihapus")
            return
        if self.head.next is None:
            hapus = self.head.no
            self.head = None
            print(f"Lagu ke-{hapus} telah terhapus")
            return
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        hapus = temp.next.no
        temp.next = None
        print(f"Lagu ke-{hapus} telah terhapus")

    def display(self):  # FIXED: Removed parameters
        if self.head is None:
            print("Playlist kosong")
            return
        
        temp = self.head
        while temp is not None:
            print(f"No. Lagu        : {temp.no}")
            print(f"Judul Lagu      : {temp.judulLagu}") # FIXED: Changed from judul to judulLagu
            print("-------------")
            temp = temp.next

#MAIN PROGRAM

l1 = LinkedList()

while True: 
    print("\n1. add new song in the playlist")
    print("2. delete first song in the playlist")
    print("3. delete last song in the playlist")
    print("4. display all songs")
    print("5. Exit")

    pilihan = int(input("Enter your choice = "))

    if pilihan == 1:
        no = int(input("Enter number: "))
        judulLagu = input("Enter judul lagu: ")
        l1.add_song(no, judulLagu)

    elif pilihan == 2:
        l1.deleteFirst()
    
    elif pilihan == 3:
        l1.deleteLast()

    elif pilihan == 4:
        l1.display()

    elif pilihan == 5:
        break