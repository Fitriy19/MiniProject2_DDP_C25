# MINI PROJECT 2
FITRI YANTI | 2309116016 | SISTEM INFORMASI

## MANAJEMEN SALON RAMBUT
## A. Deskripsi Program
Manajemen Salon Rambut adalah aplikasi Python sederhana untuk membantu Admin dan Kasir mengelola data pelanggan dengan mudah dan efisien. Menerapkan konsep CRUD (Create, Read, Update, Delete) dengan menggunakan Conditional Statements, Dictionary, Looping, Functions, dan Error Handling. Terdapat sistem login dan memiliki 2 role pengguna. Dan ada tambahan menggunakan library PrettyTable untuk menampilkan data.

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
Saat user menjalankan progam maka tampilan awalnya akan menampilkan judul yaitu "MANAJEMEN SALON RAMBUT", dan beberapa pilihan yang bisa dipilih, yaitu sebagai 1. admin, 2. kasir, dan 3. keluar.

Saat user memilih pilihan 1, program akan menampilkan pemberitahuan bahwa user memilih login sebagai Admin kemudian program meminta input username dan password dari user. Jika username dan password yang dimasukkan user benar, maka program akan menampilkan Menu Admin.  
<img width="826" height="600" alt="Screenshot 2025-09-28 004305" src="https://github.com/user-attachments/assets/1f09086a-b811-4cbb-89b7-a0407e6abc2d" />

Jika username atau password yang dimasukkan user salah, program akan menampilkan pemberitahuan login gagal. kemudian program meminta untuk menekan enter untuk kembali ke menu utama.
<img width="731" height="651" alt="Screenshot 2025-09-28 014556" src="https://github.com/user-attachments/assets/2b31e229-5f75-439d-9beb-80f5c9dbd4a0" />

Jika user memasukkan pilihan jawaban bukan diantara (1-5), program akan menampilkan pemberitahuan bahwa pilihan tidak valid, kemudian program meminta untuk menekan enter untuk kembali ke menu admin.
<img width="732" height="513" alt="Screenshot 2025-09-28 014252" src="https://github.com/user-attachments/assets/019371c4-2b5c-427d-bc61-c602655c415a" />

#### a. Read
Saat user memilih pilihan 1, program akan menampilkan pemberitahuan bahwa user memilih lihat data pelanggan kemudian akan langsung menampilkan tabel data pelanggan.
<img width="791" height="554" alt="Screenshot 2025-09-28 004822" src="https://github.com/user-attachments/assets/db78889a-525a-4293-8f3e-47ceb29ca141" />

Jika tabelnya kosong, maka program akan menampilkan pemberitahuan bahwa data pelanggan belum ada.
<img width="800" height="350" alt="Screenshot 2025-09-28 211757" src="https://github.com/user-attachments/assets/0d7975f4-e016-4a3a-a6f6-22b9f0346929" />

#### b. Create
Saat user memilih pilihan 2, program akan menampilkan pemberitahuan bahwa user memilih tambah data pelanggan, kemudian program akan meminta input nama pelanggan, layanan yang dipilih, dan harga layanannya. Jika input berhasil maka program akan langsung menampilkan tabel data pelanggan terbaru.

<img width="797" height="713" alt="Screenshot 2025-09-28 005104" src="https://github.com/user-attachments/assets/b6b0ff78-4622-4c53-b740-052c17fcf0ca" />

Jika harga yang dimasukkan bukan angka, program akan meminta input harga ulang sampai harga yang diisi user tersebut berupa angka. Baru kemudian program akan menampilkan tabel data pelanggan yang terbaru jika semua input berhasil.
<img width="734" height="725" alt="Screenshot 2025-09-28 005659" src="https://github.com/user-attachments/assets/ad892c2b-6bb6-45f7-af60-9a333cf7c8e9" />

#### c. Update
Saat user memilih pilihan 3, program akan menampilkan pemberitahuan bahwa user memilih ubah data pelanggan dan langsung menampilkan tabel data pelanggan. kemudian program akan meminta input nomor pelanggan yang ingin diubah, layanan baru, dan harga baru. Jika input berhasil maka program akan langsung menampilkan tabel data pelanggan terbaru.

<img width="721" height="822" alt="Screenshot 2025-09-28 011844" src="https://github.com/user-attachments/assets/320c685d-e1a6-40f4-ae4a-a1348cbe193a" />

Jika user memasukkan nomor yang tidak ada dalam data, program akan menampilkan pemberitahuan bahwa nomor pelanggan tidak ditemukan.   
<img width="730" height="359" alt="Screenshot 2025-09-28 012054" src="https://github.com/user-attachments/assets/d18b16d7-e3df-4504-80f7-3b40630ddf15" />

Jika nomor yang dimasukkan user bukan angka, program akan menampilkan pemberitahuan bahwa nomor harus berupa angka. Kemudian program meminta untuk menekan enter untuk kembali ke menu admin.
<img width="726" height="339" alt="Screenshot 2025-09-28 012230" src="https://github.com/user-attachments/assets/2526f9af-4234-41ac-8899-87f991de21c5" />

jika harga yang dimasukkan bukan angka, program akan meminta input harga ulang sampai harga yang diisi user tersebut berupa angka. Baru kemudian program akan menampilkan tabel data pelanggan yang terbaru jika semua input berhasil.
<img width="735" height="766" alt="Screenshot 2025-09-28 012621" src="https://github.com/user-attachments/assets/07889b64-6974-406c-ac7e-72a35ff85e46" />

#### d. Delete
Saat user memilih pilihan 4, program akan menampilkan pemberitahuan bahwa user memilih hapus data pelanggan dan langsung menampilkan tabel data pelanggan. kemudian program meminta input no. pelanggan yg ingin dihapus. Jika input berhasil maka program akan langsung menampilkan tabel data pelanggan terbaru.
<img width="726" height="770" alt="Screenshot 2025-09-28 013237" src="https://github.com/user-attachments/assets/2e73aebe-5654-41c3-a933-2ba3424eeb2e" />

Jika user memasukkan nomor yang tidak ada dalam data, program akan menampilkan pemberitahuan bahwa nomor pelanggan tidak ditemukan.    
<img width="737" height="339" alt="Screenshot 2025-09-28 013427" src="https://github.com/user-attachments/assets/ae2d9338-a52f-47a5-8571-dde21ee3008d" />

Jika nomor yang dimasukkan user bukan angka, program akan menampilkan pemberitahuan bahwa nomor harus berupa angka. Kemudian program meminta untuk menekan enter untuk kembali ke menu admin.
<img width="731" height="328" alt="Screenshot 2025-09-28 013642" src="https://github.com/user-attachments/assets/f2f6e73b-c251-4909-ad2c-1a0852768214" />

#### e. Keluar
Saat user memilih pilihan 5, program akan menampilkan pemberitahuan bahwa user memilih keluar dari menu admin dan program akan meminta menekan enter untuk kembali ke menu utama.
<img width="731" height="257" alt="Screenshot 2025-09-28 013850" src="https://github.com/user-attachments/assets/435a0a57-f104-4259-b5bb-99f723fcf83f" />

### 2. Menu Kasir
Saat user menjalankan progam maka tampilan awalnya akan menampilkan judul yaitu "MANAJEMEN SALON RAMBUT", dan beberapa pilihan yang bisa dipilih, yaitu sebagai 1. admin, 2. kasir, dan 3. keluar.

Saat user memilih pilihan 2, program akan menampilkan pemberitahuan bahwa user memilih login sebagai Kasir kemudian meminta input username dan password dari user. Jika username dan password yang dimasukkan user benar, maka program akan menampilkan Menu Kasir.
<img width="729" height="442" alt="Screenshot 2025-09-28 015030" src="https://github.com/user-attachments/assets/b1c16646-47dc-4cb8-8adf-0d5cb684ca26" />

Jika username atau password yang dimasukkan user salah, program akan menampilkan pemberitahuan login gagal. kemudian program meminta untuk menekan enter untuk kembali ke menu utama.
<img width="727" height="642" alt="Screenshot 2025-09-28 015405" src="https://github.com/user-attachments/assets/1cc135f0-33b2-4516-b522-880eddf4f973" />

Jika user memasukkan pilihan jawaban bukan diantara (1-3), program akan menampilkan pemberitahuan bahwa pilihan tidak valid, kemudian program meminta untuk menekan enter untuk kembali ke menu kasir.
<img width="731" height="243" alt="Screenshot 2025-09-28 021049" src="https://github.com/user-attachments/assets/67d26dad-74cf-4ced-960f-56ac21461004" />

#### a. Read
Saat user memilih pilihan 1, program akan menampilkan pemberitahuan bahwa user memilih lihat data pelanggan kemudian akan langsung menampilkan tabel data pelanggan.

<img width="730" height="446" alt="Screenshot 2025-09-28 020041" src="https://github.com/user-attachments/assets/58625b6d-95fc-4244-a30b-d0a22553c158" />

Jika tabelnya kosong, maka program akan menampilkan pemberitahuan bahwa data pelanggan belum ada.

<img width="795" height="311" alt="Screenshot 2025-09-28 211853" src="https://github.com/user-attachments/assets/069c91c6-5602-4e93-a7e5-8cee39744877" />

#### b. Create
Saat user memilih pilihan 2, program akan menampilkan pemberitahuan bahwa user memilih tambah data pelanggan, kemudian program akan meminta input nama pelanggan, layanan yang dipilih, dan harga layanannya. Jika input berhasil maka program akan langsung menampilkan tabel data pelanggan terbaru.

<img width="727" height="574" alt="Screenshot 2025-09-28 020308" src="https://github.com/user-attachments/assets/dc6e6321-9a99-430d-9f33-3620ec4c0ef6" />

Jika harga yang dimasukkan bukan angka, program akan meminta input harga ulang sampai harga yang diisi user tersebut berupa angka. Baru kemudian program akan menampilkan tabel data pelanggan yang terbaru. jika semua input berhasil.
<img width="732" height="694" alt="Screenshot 2025-09-28 020715" src="https://github.com/user-attachments/assets/13d17723-6332-4707-bcbc-4355e6a52fd7" />

#### c. Keluar
Saat user memilih pilihan 3, program akan menampilkan pemberitahuan bahwa user memilih keluar dari menu kasir dan program akan meminta menekan enter untuk kembali ke menu utama.
<img width="735" height="209" alt="Screenshot 2025-09-28 020938" src="https://github.com/user-attachments/assets/4ed47eac-f9cc-4e27-9883-60e8ed562541" />

### 3. Keluar dari Menu Utama
Saat user memilih pilihan 3, program akan menampilkan pemberitahuan bahwa user memilih keluar dari Menu Utama dan program akan langsung berhenti.

<img width="732" height="209" alt="Screenshot 2025-09-28 021207" src="https://github.com/user-attachments/assets/e202b28a-8006-4624-bc6a-3e4081bc78b4" />

Jika user memasukkan pilihan jawaban bukan diantara (1-3), program akan menampilkan pemberitahuan bahwa pilihan tidak valid, kemudian program meminta untuk menekan enter untuk kembali.     
<img width="729" height="465" alt="Screenshot 2025-09-28 021459" src="https://github.com/user-attachments/assets/53135cc2-9299-4f1d-9c40-17a11dc336be" />

### Tambahan:
Setelah setiap proses, program akan meminta pengguna menekan Enter agar hasil output bisa dibaca dengan jelas sebelum kembali ke menu admin, kasir, maupun menu utama.

<img width="733" height="208" alt="Screenshot 2025-09-28 021813" src="https://github.com/user-attachments/assets/185b509d-ee82-4a32-9618-e2b432071eb8" />

<img width="733" height="186" alt="Screenshot 2025-09-28 021939" src="https://github.com/user-attachments/assets/ba5dc288-79f7-41d0-a870-b6f758c23496" />

<img width="734" height="235" alt="Screenshot 2025-09-28 022104" src="https://github.com/user-attachments/assets/13ad9619-bbb1-452f-8872-41d9c8781ea7" />

<img width="732" height="200" alt="Screenshot 2025-09-28 022208" src="https://github.com/user-attachments/assets/e69664d6-e17e-44d2-a11f-139626ba8aef" />
