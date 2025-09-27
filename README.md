# MINI PROJECT 2
FITRI YANTI | 2309116016 | SISTEM INFORMASI

## MANAJEMEN SALON RAMBUT
## A. Deskripsi Program
Manajemen Salon Rambut adalah aplikasi Python sederhana untuk membantu pemilik salon atau admin mengelola data pelanggan dengan mudah dan efisien. Menerapkan konsep CRUD (Create, Read, Update, Delete) dengan menggunakan Conditional Statements, Dictionary, Looping, Functions, dan Error Handling. Terdapat sistem login dan memiliki 2 role pengguna. Dan ada tambahan menggunakan library PrettyTable untuk menampilkan data.

## B. Flowchart
<img width="2168" height="2935" alt="minpro_2 drawio" src="https://github.com/user-attachments/assets/f56e47bc-3937-4902-ac39-fbe2b0835a71" />

## C. Fitur Program
- Login: User memilih peran Admin atau Kasir, lalu memasukkan username dan password. Sistem memeriksa kecocokan username, password, dan role.
- Lihat Data Pelanggan: Menampilkan seluruh data pelanggan dalam tabel.
- Tambah Data Pelanggan: Menambahkan data pelanggan baru dengan nomor otomatis.
- Ubah Data Pelanggan: Mengubah layanan dan harga pelanggan berdasarkan nomor.
- Hapus Data Pelanggan: Menghapus data pelanggan berdasarkan nomor.
- Keluar: Menutup program atau kembali ke menu login.

## D. Struktur Kode
- users: Menyimpan username, password, dan role untuk login.
- data_pelanggan: Menyimpan data pelanggan dengan nomor sebagai kunci.
- login(): Memeriksa input login sesuai role.
- tampilkan_pelanggan(): Menampilkan data pelanggan dalam tabel.
- tambah_pelanggan(): Menambahkan pelanggan baru dengan nomor otomatis.
- ubah_pelanggan(): Mengubah layanan dan harga pelanggan.
- hapus_pelanggan(): Menghapus data pelanggan.
- Menu Utama: Perulangan pilihan fitur hingga user memilih keluar.

## E. Penjelasan Output
### 1. Login
### 2. Menu Admin
#### a. Read
#### b. Create
#### c. Update
#### d. Delete
#### e. Keluar
### 3. Menu Kasir
#### a. Read
#### b. Create
#### c. Keluar
### 4. Keluar
### Tambahan:
Setelah setiap proses, program akan meminta pengguna menekan Enter agar hasil output bisa dibaca dengan jelas sebelum kembali ke menu utama.
