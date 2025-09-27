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
### 1. Menu Admin
tampilan awal. penjelasan.
<img width="826" height="600" alt="Screenshot 2025-09-28 004305" src="https://github.com/user-attachments/assets/1f09086a-b811-4cbb-89b7-a0407e6abc2d" />

jika usn/pass salah.
<img width="731" height="651" alt="Screenshot 2025-09-28 014556" src="https://github.com/user-attachments/assets/2b31e229-5f75-439d-9beb-80f5c9dbd4a0" />

jika pilihan yang dimasukkan bukan dari 1-5

<img width="732" height="513" alt="Screenshot 2025-09-28 014252" src="https://github.com/user-attachments/assets/019371c4-2b5c-427d-bc61-c602655c415a" />



#### a. Read
penjelasan.

<img width="791" height="554" alt="Screenshot 2025-09-28 004822" src="https://github.com/user-attachments/assets/db78889a-525a-4293-8f3e-47ceb29ca141" />

Jika tabelnya kosong, maka program akan menampilkan output “data pelanggan belum ada”.
(gambar)


#### b. Create
p.

<img width="797" height="713" alt="Screenshot 2025-09-28 005104" src="https://github.com/user-attachments/assets/b6b0ff78-4622-4c53-b740-052c17fcf0ca" />

jika harga yang dimasukkan bukan angka.
<img width="734" height="725" alt="Screenshot 2025-09-28 005659" src="https://github.com/user-attachments/assets/ad892c2b-6bb6-45f7-af60-9a333cf7c8e9" />

#### c. Update
p.

<img width="721" height="822" alt="Screenshot 2025-09-28 011844" src="https://github.com/user-attachments/assets/320c685d-e1a6-40f4-ae4a-a1348cbe193a" />

jika no pelanggan tidak ditemukan

<img width="730" height="359" alt="Screenshot 2025-09-28 012054" src="https://github.com/user-attachments/assets/d18b16d7-e3df-4504-80f7-3b40630ddf15" />

jika nomor yg dimasukkan bukan angka

<img width="726" height="339" alt="Screenshot 2025-09-28 012230" src="https://github.com/user-attachments/assets/2526f9af-4234-41ac-8899-87f991de21c5" />

jika harga yang dimasukkan bukan angka
<img width="735" height="766" alt="Screenshot 2025-09-28 012621" src="https://github.com/user-attachments/assets/07889b64-6974-406c-ac7e-72a35ff85e46" />

#### d. Delete
p.

<img width="726" height="770" alt="Screenshot 2025-09-28 013237" src="https://github.com/user-attachments/assets/2e73aebe-5654-41c3-a933-2ba3424eeb2e" />

jika nomor tidak ada

<img width="726" height="770" alt="Screenshot 2025-09-28 013237" src="https://github.com/user-attachments/assets/e64f78ba-bd65-4b9a-b530-d6f5f400abd4" />

jika nomor yang dimasukkan bukan angka

<img width="731" height="328" alt="Screenshot 2025-09-28 013642" src="https://github.com/user-attachments/assets/f2f6e73b-c251-4909-ad2c-1a0852768214" />

#### e. Keluar
p

<img width="731" height="257" alt="Screenshot 2025-09-28 013850" src="https://github.com/user-attachments/assets/435a0a57-f104-4259-b5bb-99f723fcf83f" />


### 2. Menu Kasir
p

<img width="729" height="442" alt="Screenshot 2025-09-28 015030" src="https://github.com/user-attachments/assets/b1c16646-47dc-4cb8-8adf-0d5cb684ca26" />

jika usn/pass salah
<img width="727" height="642" alt="Screenshot 2025-09-28 015405" src="https://github.com/user-attachments/assets/1cc135f0-33b2-4516-b522-880eddf4f973" />

jika pilihan bukan dari 1-3
<img width="731" height="243" alt="Screenshot 2025-09-28 021049" src="https://github.com/user-attachments/assets/67d26dad-74cf-4ced-960f-56ac21461004" />


#### a. Read
p

<img width="730" height="446" alt="Screenshot 2025-09-28 020041" src="https://github.com/user-attachments/assets/58625b6d-95fc-4244-a30b-d0a22553c158" />

jika kosong

#### b. Create
p

<img width="727" height="574" alt="Screenshot 2025-09-28 020308" src="https://github.com/user-attachments/assets/dc6e6321-9a99-430d-9f33-3620ec4c0ef6" />

jika harga bukan angka
<img width="732" height="694" alt="Screenshot 2025-09-28 020715" src="https://github.com/user-attachments/assets/13d17723-6332-4707-bcbc-4355e6a52fd7" />


#### c. Keluar
<img width="735" height="209" alt="Screenshot 2025-09-28 020938" src="https://github.com/user-attachments/assets/4ed47eac-f9cc-4e27-9883-60e8ed562541" />


### 3. Keluar
<img width="732" height="209" alt="Screenshot 2025-09-28 021207" src="https://github.com/user-attachments/assets/e202b28a-8006-4624-bc6a-3e4081bc78b4" />

jika pilihan bukan dari 1-3
<img width="729" height="465" alt="Screenshot 2025-09-28 021459" src="https://github.com/user-attachments/assets/53135cc2-9299-4f1d-9c40-17a11dc336be" />


### Tambahan:
Setelah setiap proses, program akan meminta pengguna menekan Enter agar hasil output bisa dibaca dengan jelas sebelum kembali ke menu utama.

<img width="733" height="208" alt="Screenshot 2025-09-28 021813" src="https://github.com/user-attachments/assets/185b509d-ee82-4a32-9618-e2b432071eb8" />

<img width="733" height="186" alt="Screenshot 2025-09-28 021939" src="https://github.com/user-attachments/assets/ba5dc288-79f7-41d0-a870-b6f758c23496" />

<img width="734" height="235" alt="Screenshot 2025-09-28 022104" src="https://github.com/user-attachments/assets/13ad9619-bbb1-452f-8872-41d9c8781ea7" />

<img width="732" height="200" alt="Screenshot 2025-09-28 022208" src="https://github.com/user-attachments/assets/e69664d6-e17e-44d2-a11f-139626ba8aef" />
