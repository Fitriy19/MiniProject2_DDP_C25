from prettytable import PrettyTable

users = {
    "admin22": {"password": "777", "role": "Admin"},
    "kasir9": {"password": "999", "role": "Kasir"}
}

data_pelanggan = {
    1: {"nama": "amel", "layanan": "potong rambut", "harga": 25000},
    2: {"nama": "aya", "layanan": "creambath", "harga": 90000},
    3: {"nama": "sabilla", "layanan": "hair coloring", "harga": 120000},
    4: {"nama": "dila", "layanan": "smoothing", "harga": 170000}
}

#Read
def tampilkan_pelanggan():
    print("\n============ Data Pelanggan ==============")
    if data_pelanggan:
        tabel = PrettyTable()
        tabel.field_names = ["No.", "Nama", "Layanan", "Harga"]
        for no, data in data_pelanggan.items():
            tabel.add_row([no, data['nama'], data['layanan'], data['harga']])
        print(tabel)
    else:
        print("\n--Data pelanggan belum ada--")

#Create
def tambah_pelanggan():
    nama = input("\nMasukkan nama pelanggan: ")
    layanan = input("Masukkan layanan yang dipilih: ")
    while True:
        try:
            harga = int(input("Masukkan harga layanan: "))
            break
        except ValueError:
            print("\n--Harga harus berupa angka!--")
    no_baru = max(data_pelanggan.keys(), default=0) + 1
    data_pelanggan[no_baru] = {"nama": nama, "layanan": layanan, "harga": harga}
    print("\n---Data pelanggan berhasil ditambahkan---")
    tampilkan_pelanggan()

#Update
def ubah_pelanggan():
    try:
        no = int(input("\nMasukkan No. pelanggan yang ingin diubah: "))
        if no in data_pelanggan:
            layanan_baru = input("Masukkan layanan baru: ")
            while True:
                try:
                    harga_baru = int(input("Masukkan harga baru: "))
                    break
                except ValueError:
                    print("\n--Harga harus berupa angka!--")
            data_pelanggan[no]["layanan"] = layanan_baru
            data_pelanggan[no]["harga"] = harga_baru
            print("\n---Data pelanggan berhasil diubah---")
            tampilkan_pelanggan()
        else:
            print("--No. pelanggan tidak ditemukan--")
    except ValueError:
        print("--Nomor harus berupa angka!--")

#Delete
def hapus_pelanggan():
    try:
        no = int(input("\nMasukkan No. pelanggan yang ingin dihapus: "))
        if no in data_pelanggan:
            del data_pelanggan[no]
            print("\n---Data pelanggan berhasil dihapus---")
            tampilkan_pelanggan()
        else:
            print("--No. pelanggan tidak ditemukan--")
    except ValueError:
        print("--Nomor harus berupa angka!--")

#Login
def login(role):
    username = input("\nMasukkan username : ")
    password = input("Masukkan password : ")
    if (
        username in users
        and users[username]["password"] == password
        and users[username]["role"] == role
    ):
        print("\nLogin Berhasil!")
        print(f"------- Selamat datang di Menu {role} --------")
        return True
    else:
        return False

#Menu Admin
def menu_admin():
    while True:
        print("=============================================")
        print("|                MENU ADMIN                 |")
        print("=============================================")
        print("|  1. Lihat Data Pelanggan                  |")
        print("|  2. Tambah Data Pelanggan                 |")
        print("|  3. Ubah Data Pelanggan                   |")
        print("|  4. Hapus Data Pelanggan                  |")
        print("|  5. Keluar                                |")
        print("=============================================")
        pilihan = input("Masukkan pilihan Anda (1-5): ")
        if pilihan == "1":
            print("\n==== Anda memilih Lihat data pelanggan ====")
            tampilkan_pelanggan()
            input("\nTekan Enter untuk kembali..\n")
        elif pilihan == "2":
            print("\n==== Anda memilih Tambah data pelanggan ====")
            tambah_pelanggan()
            input("\nTekan Enter untuk kembali..\n")
        elif pilihan == "3":
            print("\n==== Anda memilih Ubah data pelanggan ====")
            tampilkan_pelanggan()
            ubah_pelanggan()
            input("\nTekan Enter untuk kembali..\n")
        elif pilihan == "4":
            print("\n==== Anda memilih Hapus data pelanggan ====")
            tampilkan_pelanggan()
            hapus_pelanggan()
            input("\nTekan Enter untuk kembali..\n")
        elif pilihan == "5":
            print("\n==== Anda memilih keluar dari menu Admin ====")
            input("Tekan Enter untuk kembali ke menu utama..")
            break
        else:
            print("\n--Pilihan tidak valid, hanya pilih diantara 1-5--")
            input("Tekan Enter untuk kembali..\n")

#Menu Kasir
def menu_kasir():
    while True:
        print("=============================================")
        print("|                MENU KASIR                 |")
        print("=============================================")
        print("|  1. Lihat Data Pelanggan                  |")
        print("|  2. Tambah Data Pelanggan                 |")
        print("|  3. Keluar                                |")
        print("=============================================")
        pilihan = input("Masukkan pilihan Anda (1-3): ")
        if pilihan == "1":
            print("\n==== Anda memilih Lihat data pelanggan ====")
            tampilkan_pelanggan()
            input("\nTekan Enter untuk kembali..\n")
        elif pilihan == "2":
            print("\n==== Anda memilih Tambah data pelanggan ====")
            tambah_pelanggan()
            input("\nTekan Enter untuk kembali..\n")
        elif pilihan == "3":
            print("\n==== Anda memilih keluar dari menu Kasir ====")
            input("Tekan Enter untuk kembali ke menu utama..")
            break
        else:
            print("\n--Pilihan tidak valid, hanya pilih diantara 1-3--")
            input("\nTekan Enter untuk kembali..\n")

#Menu Utama
if __name__ == "__main__":
    while True:
        print("\n=============================================")
        print("|          MANAJEMEN SALON RAMBUT           |")
        print("=============================================")
        print("|  1. Admin                                 |")
        print("|  2. Kasir                                 |")
        print("|  3. Keluar                                |")
        print("=============================================")
        pilihan_role = input("Anda ingin masuk sebagai apa? Masukkan pilihan Anda: ")
        if pilihan_role == "1":
            print("\n==== Anda memilih login sebagai Admin ====")
            if login("Admin"):
                menu_admin()
            else:
                print("\n--Login gagal. Username atau password Anda salah--")
                input("\nTekan Enter untuk kembali..")
        elif pilihan_role == "2":
            print("\n==== Anda memilih login sebagai Kasir ====")
            if login("Kasir"):
                menu_kasir()
            else:
                print("\n--Login gagal. Username atau password Anda salah--")
                input("\nTekan Enter untuk kembali..")
        elif pilihan_role == "3":
            print("\n=== Anda memilih keluar dari menu utama. Terima kasih ===")
            break
        else:
            print("\n--Pilihan tidak valid, hanya pilih diantara 1-3--")
            input("\nTekan Enter untuk kembali..")
