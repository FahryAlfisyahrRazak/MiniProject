data_absensi = []
daftar_nama = ("Adnan", "Alfi", "Miko", "Daffa")
 
print("SISTEM ABSENSI KELAS")
 
while True:
    print("MENU")
    print("1. Tambah Data Absensi")
    print("2. Tampilkan Semua Data")
    print("3. Ubah Data Absensi")
    print("4. Hapus Data Absensi")
    print("5. Keluar")
 
    pilihan = input("Pilih menu [1-5]: ")
 
    if pilihan == "1":
        print("Daftar Nama:", daftar_nama)
        nama = input("Masukkan Nama: ")
 
        if nama not in daftar_nama:
            print("Nama tidak ada di daftar!")
            continue
 
        status = input("Masukkan Status [Hadir/Izin/Alpha]: ")
        if status != "Hadir" and status != "Izin" and status != "Alpha":
            print("Status tidak valid!")
            continue
 
        pertemuan = input("Pertemuan ke-: ")
        if not pertemuan.isdigit():
            print("Pertemuan harus angka!")
            continue
        pertemuan = int(pertemuan)
 
        data_baru = (nama, status, pertemuan)
        data_absensi.append(data_baru)
        print("Data berhasil ditambahkan!")
 
    elif pilihan == "2":
        print("DATA ABSENSI")
        if len(data_absensi) == 0:
            print("Data masih kosong")
        else:
            print("No | Nama | Status | Pertemuan")
            no = 1
            for data in data_absensi:
                print(no, "|", data[0], "|", data[1], "|", data[2])
                no += 1
 
    elif pilihan == "3":
        if len(data_absensi) == 0:
            print("Data kosong, tidak bisa diubah")
            continue
 
        no = input("Masukkan nomor data yang mau diubah: ")
        if not no.isdigit():
            print("Input salah!")
            continue
 
        no = int(no) - 1
        if no < 0 or no >= len(data_absensi):
            print("Nomor tidak valid")
            continue
 
        nama_baru = input("Nama baru: ")
        status_baru = input("Status baru [Hadir/Izin/Alpha]: ")
        pertemuan_baru = input("Pertemuan baru: ")
        if not pertemuan_baru.isdigit():
            print("Input salah!")
            continue
 
        data_absensi[no] = (nama_baru, status_baru, int(pertemuan_baru))
        print("Data berhasil diubah!")
 
    elif pilihan == "4":
        if len(data_absensi) == 0:
            print("Data kosong, tidak bisa dihapus")
            continue
 
        no = input("Masukkan nomor data yang mau dihapus: ")
        if not no.isdigit():
            print("Input salah!")
            continue
 
        no = int(no) - 1
        if no < 0 or no >= len(data_absensi):
            print("Nomor tidak valid")
            continue
 
        hapus = data_absensi.pop(no)
        print("Data", hapus, "berhasil dihapus!")
 
    elif pilihan == "5":
        print("Program selesai")
        break
 
    else:
        print("Menu tidak valid, pilih 1-5")