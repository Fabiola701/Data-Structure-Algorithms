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