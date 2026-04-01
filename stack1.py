stack = []

stack.append("Data1")
stack.append("Data2")
stack.append("Data3")
print("Stack after pushing 3 data: ", stack)

hapus = stack.pop()
print("Data yang dihapus: ", hapus)

print("Isi stack terakhir: ", stack)

# Data yang terhapus: Data3
# Isi stack terakhir: ['Data1', 'Data2']

# karena stack menggunakan prinsip LIFO (Last In, First Out), 
# data yang terakhir dimasukkan (Data3) adalah yang pertama dihapus saat kita melakukan pop. 
# Setelah Data3 dihapus, stack hanya menyisakan Data1 dan Data2.

# Jawaban soal No.2
buku = []

buku.append("Matematika")
buku.append("Fisika")
buku.append("Kimia")
buku.append("Biologi")
print("Stack awal:", buku)

hapus1 = buku.pop()
hapus2 = buku.pop()

print("Buku yang dihapus:", hapus1, "dan", hapus2)

print("Isi stack sekarang:", buku)
# Jika "Sejarah" ditambahkan, dia ada di posisi paling atas (index -1/top of stack)
# karena append() selalu menambahkan di akhir

# Jawaban soal No.3
data = []

if len(data) == 0:
    print("stack masih kosong")

data.append("10")
data.append("20")

print("tampilkan isi stack: ", data)

#hapus semua isi stack (bisa pakai clear() atau pop() sampai kosong)
data.pop()
data.pop()

#cek kembali apakah stack kosong
if len(data) == 0:
    print("stack sudah kosong")
else:
    print("stack masih ada isinya: ", data)



# Jawaban soal No.4
# stack dengan menu

stack = []

while True:
    print("\n --- Menu Stack ---")
    print("1. Push (Tambah Data)")
    print("2. Pop (Hapus Data)")
    print("3. Lihat Stack")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = input("Masukkan data untuk ditambahkan ke stack: ")
        stack.append(data)
        print(f"'{data}' berhasil ditambahkan ke stack.")

    elif pilihan == "2":
        if len(stack) == 0:
            print("Stack kosong! Tidak ada data untuk dihapus.")
        else:
            dataHapus = stack.pop()
            print(f"'{dataHapus}' berhasil dihapus dari stack.")

    elif pilihan == "3":
        if len(stack) == 0:
            print("Stack masih kosong")
        else:
            print("Isi stack: ", stack)
    
    elif pilihan == "4":
        print("keluar dari program.")
        break
    else:
        print("option is not valid")