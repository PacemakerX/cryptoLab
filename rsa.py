import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_prime(start=100, end=300):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi

    while e > 0:
        q = temp_phi // e
        temp1 = temp_phi - q * e
        temp_phi, e = e, temp1

        x = x2 - q * x1
        y = d - q * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    return d + phi if d < 0 else d

def generate_keys():
    print("Generating two random prime numbers...")
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    print("Prime numbers selected:")
    print(f"p = {p}, q = {q}")

    n = p * q
    phi = (p - 1) * (q - 1)

    print(f"n = p * q = {n}")
    print(f"Euler's Totient (phi) = {phi}")

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)

    print(f"Public exponent (e) = {e}")
    print(f"Private exponent (d) = {d}")

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# ==== Main Program ====
print("=== RSA Encryption-Decryption ===")
message = input("Enter the message to encrypt: ")

# Generate keys
public, private = generate_keys()

# Encrypt
encrypted = encrypt(public, message)
print("\nEncrypted message (as numbers):")
print(encrypted)

# Decrypt
decrypted = decrypt(private, encrypted)
print("\nDecrypted message:")
print(decrypted)
