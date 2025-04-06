def generate_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []

    for c in key:
        if c not in seen and c.isalpha():
            matrix.append(c)
            seen.add(c)

    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in seen:
            matrix.append(c)
            seen.add(c)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return -1, -1

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            cipher += matrix[r1][c2] + matrix[r2][c1]

    return cipher

def playfair_decrypt(cipher, key):
    matrix = generate_matrix(key)
    plain = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            plain += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plain += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            plain += matrix[r1][c2] + matrix[r2][c1]

    return plain

# === MAIN ===
print("---- Playfair Cipher ----")
key = input("Enter key: ")
text = input("Enter message: ")

cipher = playfair_encrypt(text, key)
print("Encrypted Text:", cipher)

plain = playfair_decrypt(cipher, key)
print("Decrypted Text:", plain)
