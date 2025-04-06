def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mult(A, B):
    return [
        (A[0]*B[0] + A[1]*B[2]) % 26,
        (A[0]*B[1] + A[1]*B[3]) % 26,
        (A[2]*B[0] + A[3]*B[2]) % 26,
        (A[2]*B[1] + A[3]*B[3]) % 26
    ]

def encrypt(message, key):
    message = message.upper().replace(" ", "")
    if len(message) % 2 != 0:
        message += 'X'
    
    encrypted = ''
    for i in range(0, len(message), 2):
        a = ord(message[i]) - ord('A')
        b = ord(message[i+1]) - ord('A')
        x = (key[0]*a + key[1]*b) % 26
        y = (key[2]*a + key[3]*b) % 26
        encrypted += chr(x + ord('A')) + chr(y + ord('A'))
    return encrypted

def decrypt(cipher, key):
    det = (key[0]*key[3] - key[1]*key[2]) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        return "Key not invertible."

    # Adjoint of 2x2 matrix
    adj = [key[3], -key[1], -key[2], key[0]]
    inv_key = [(det_inv * adj[i]) % 26 for i in range(4)]

    decrypted = ''
    for i in range(0, len(cipher), 2):
        a = ord(cipher[i]) - ord('A')
        b = ord(cipher[i+1]) - ord('A')
        x = (inv_key[0]*a + inv_key[1]*b) % 26
        y = (inv_key[2]*a + inv_key[3]*b) % 26
        decrypted += chr(x + ord('A')) + chr(y + ord('A'))
    return decrypted

# === MAIN ===
print("---- Hill Cipher (2x2) ----")
msg = input("Enter message: ")
key = list(map(int, input("Enter 4 numbers (2x2 key matrix): ").split()))

cipher = encrypt(msg, key)
print("Encrypted Text:", cipher)

plain = decrypt(cipher, key)
print("Decrypted Text:", plain)
    