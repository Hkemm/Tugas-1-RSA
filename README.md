Deskripsi

Program ini merupakan implementasi sederhana algoritma kriptografi RSA (Rivest–Shamir–Adleman) menggunakan bahasa Python. RSA adalah algoritma kriptografi kunci publik yang digunakan untuk proses enkripsi dan dekripsi data.

Program ini mencakup:

Generate bilangan prima

Pembangkitan public key dan private key

Proses enkripsi

Proses dekripsi

Extended Euclidean Algorithm untuk mencari modular inverse

⚠️ Catatan: Implementasi ini hanya untuk pembelajaran dan menggunakan bilangan prima kecil sehingga tidak aman untuk penggunaan nyata.

🧠 Konsep Dasar RSA

Pilih dua bilangan prima p dan q

Hitung:

n = p × q

Hitung fungsi totien Euler:

φ(n) = (p − 1)(q − 1)

Pilih nilai e sehingga:

gcd(e, φ(n)) = 1

Hitung nilai d:

d ≡ e⁻¹ mod φ(n)

Enkripsi:

C = M^e mod n

Dekripsi:

M = C^d mod n
📂 Struktur Program
1️⃣ Cek Bilangan Prima
def is_prime(n):

Mengecek apakah suatu angka merupakan bilangan prima menggunakan metode sederhana (cek hingga √n).

2️⃣ Generate Bilangan Prima
def generate_prime(start=100, end=300):

Menghasilkan bilangan prima acak dalam rentang tertentu.

3️⃣ Extended Euclidean Algorithm
def egcd(a, b):

Digunakan untuk menghitung:

gcd(a, b)

Koefisien Bézout

Modular inverse

4️⃣ Modular Inverse
def modinv(e, phi):

Menghitung nilai d sehingga:

(e × d) mod φ(n) = 1
🔑 Proses Key Generation

Langkah-langkah:

Generate p dan q

Hitung n dan φ(n)

Tentukan nilai e (default: 65537)

Hitung d menggunakan modular inverse

Output:

Public Key  = (e, n)
Private Key = (d, n)
🔒 Proses Enkripsi
ciphertext = pow(message, e, n)

Menggunakan fungsi bawaan Python:

pow(base, exponent, modulus)

Rumus:

C = M^e mod n
🔓 Proses Dekripsi
decrypted = pow(ciphertext, d, n)

Rumus:

M = C^d mod n

Jika berhasil, hasil dekripsi akan sama dengan plaintext awal.

▶️ Cara Menjalankan Program

Pastikan Python 3 sudah terinstall

Simpan file sebagai:

rsa.py

Jalankan di terminal:

python rsa.py
🖥️ Contoh Output
p = 137
q = 193
n = 26441
phi(n) = 26112
Public Key (e, n) = (65537, 26441)
Private Key (d, n) = (9377, 26441)

Plaintext: 42
Ciphertext: 12345
Decrypted: 42

✅ Kelebihan

Mudah dipahami

Struktur kode modular

Menggunakan konsep matematika lengkap RSA

Cocok untuk tugas kuliah / praktikum keamanan data

❌ Keterbatasan

Menggunakan bilangan prima kecil

Tidak menggunakan padding (seperti OAEP)

Tidak aman untuk aplikasi produksi

📌 Tujuan

Program ini dibuat untuk:

1.Memahami konsep kriptografi kunci publik

2.Memahami operasi modular arithmetic

3.Memahami Extended Euclidean Algorithm

4.Kebutuhan tugas/praktikum keamanan data
