class Stack:
    def __init__(self):
        self.stack = [] # nama list untuk menyimpan elemen stack
    def push(self,data):
        self.stack.append(data)
        print(f"Data '{data}' berhasil ditambahkan ke stack.")
    def pop(self):
        p = self.stack[-1] # mengambil elemen terakhir dari stack
        self.stack.pop() # menghapus elemen terakhir dari stack
        print(f"Data yang di-pop: {p}")
    def peek(self):
        print(f"Data teratas di stack: {self.stack[-1]}") # menampilkan elemen terakhir dari stack
    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack kosong")
        else:
            print("Stack tidak kosong")
    def size(self):
        print(f"Jumlah elemen di stack: {len(self.stack)}")
    def display(self):
        print("Isi stack:", self.stack)

#MAIN PROGRAM
stack1 = Stack()
while True:
    print("\n--- Menu Stack ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Empty")
    print("5. Size")
    print("6. Display")
    print("7. Keluar")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
        data = input("Masukkan data untuk ditambahkan ke stack: ")
        stack1.push(data)

    elif pilihan == 2:
        stack1.pop()

    elif pilihan == 3:
        stack1.peek()

    elif pilihan == 4:
        stack1.isEmpty()

    elif pilihan == 5:
        stack1.size()

    elif pilihan == 6:
        stack1.display()

    elif pilihan == 7:
        print("Keluar dari program.")
        break
    else:
        print("invalid input")
    
#namaObject = namaClass()
# stack1 = Stack() # membuat objek stack1 dari class Stack
# stack2 = Stack() # membuat objek stack2 dari class Stack
# stack2.push(10) # memanggil method push() pada objek stack2 untuk menambahkan data 10 ke stack

#berikut kita akan bahas, bagaimana mencari problem and gunakan stack untuk menyelesaikan problem tersebut, yaitu dengan menggunakan stack untuk membalikkan sebuah string.
    


    