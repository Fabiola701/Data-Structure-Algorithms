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