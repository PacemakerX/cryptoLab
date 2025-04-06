import hashlib
import random

# Check if a number is prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

# Generate small prime q
def generate_prime_q():
    while True:
        q = random.randint(100, 200)
        if is_prime(q):
            return q

# Modular inverse (brute-force for small q)
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Generate keys: public and private
def generate_keys():
    q = generate_prime_q()
    p = q * random.randint(5, 10) + 1
    while not is_prime(p):
        p += 1
    h = random.randint(2, p - 2)
    g = pow(h, (p - 1) // q, p)
    x = random.randint(1, q - 1)       # Private key
    y = pow(g, x, p)                   # Public key

    return (p, q, g, y), x

# Hash the message using SHA-1
def hash_message(msg):
    h = hashlib.sha1(msg.encode()).hexdigest()
    return int(h, 16)

# Sign the message
def sign_message(msg, x, p, q, g):
    hm = hash_message(msg) % q
    while True:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = modinv(k, q)
        s = (k_inv * (hm + x * r)) % q
        if s != 0:
            break
    return r, s

# Verify the signature
def verify_signature(msg, r, s, y, p, q, g):
    if not (0 < r < q and 0 < s < q):
        return False

    hm = hash_message(msg) % q
    w = modinv(s, q)
    u1 = (hm * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    return v == r

# === MAIN PROGRAM ===
print("----- DSA Digital Signature Simulation -----")
msg = input("Enter a message to sign: ")

# Key generation
(pub_key, priv_key) = generate_keys()
(p, q, g, y) = pub_key
x = priv_key

print("\nGenerated Keys:")
print(f"Public Key -> p: {p}, q: {q}, g: {g}, y: {y}")
print(f"Private Key -> x: {x}")

# Signing
r, s = sign_message(msg, x, p, q, g)
print("\nSignature:")
print(f"r: {r}")
print(f"s: {s}")

# Verification
print("\n----- Verification -----")
msg_check = input("Enter message to verify signature: ")
r_check = int(input("Enter r: "))
s_check = int(input("Enter s: "))

valid = verify_signature(msg_check, r_check, s_check, y, p, q, g)

print("\nVerification Result:")
print("Signature is VALID ✅" if valid else "Signature is INVALID ❌")
