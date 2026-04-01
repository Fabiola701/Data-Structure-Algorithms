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