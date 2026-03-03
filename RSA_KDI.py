import random
import math

# Cek bilangan prima (sederhana)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate bilangan prima kecil 
def generate_prime(start=100, end=300):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Modular inverse
def modinv(e, phi):
    gcd, x, _ = egcd(e, phi)
    if gcd != 1:
        raise Exception("e dan phi(n) tidak relatif prima")
    return x % phi

# === Key Generation ===
p = generate_prime()
q = generate_prime()
while p == q:
    q = generate_prime()

n = p * q
phi = (p - 1) * (q - 1)

e = 65537  # nilai umum
if math.gcd(e, phi) != 1:
    e = 3
    while math.gcd(e, phi) != 1:
        e += 2

d = modinv(e, phi)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi(n) =", phi)
print("Public Key (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))

# === Enkripsi ===
message = 42  # plaintext (angka kecil)
ciphertext = pow(message, e, n)
print("\nPlaintext:", message)
print("Ciphertext:", ciphertext)

# === Dekripsi ===
decrypted = pow(ciphertext, d, n)
print("Decrypted:", decrypted)