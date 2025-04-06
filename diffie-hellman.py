def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Publicly shared values
P = int(input("Enter a prime number (P): "))
G = int(input("Enter a primitive root modulo P (G): "))

# Private keys
a = int(input("Enter Private Key for User A: "))
b = int(input("Enter Private Key for User B: "))

# Calculating public keys
x = power(G, a, P)  # A's public key
y = power(G, b, P)  # B's public key

# Exchanging and calculating shared secret
keyA = power(y, a, P)  # A receives y
keyB = power(x, b, P)  # B receives x

print(f"\nUser A's Public Key: {x}")
print(f"User B's Public Key: {y}")
print(f"Shared Secret Key (A's side): {keyA}")
print(f"Shared Secret Key (B's side): {keyB}")
