from mahasiswa import Mahasiswa

daftar_mahasiswa = []


def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    mhs = Mahasiswa(nim, nama, jurusan)
    daftar_mahasiswa.append(mhs)
    print("✅ Mahasiswa berhasil ditambahkan.\n")


def tampilkan_mahasiswa():
    if not daftar_mahasiswa:
        print("⚠️  Belum ada data mahasiswa.\n")
        return
    print("\n=== Daftar Mahasiswa ===")
    for idx, mhs in enumerate(daftar_mahasiswa, start=1):
        print(f"{idx}. {mhs}")
    print()


def menu():
    while True:
        print("===== Menu Aplikasi Mahasiswa =====")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        print()

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            print("👋 Terima kasih!")
            break
        else:
            print("❌ Pilihan tidak valid.\n")


if __name__ == "__main__":
    menu()


