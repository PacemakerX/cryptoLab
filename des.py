# === Any-size S-box ===
s_box = [
    [0x6, 0xB, 0x0, 0x4],
    [0x3, 0xF, 0x8, 0x1],
    [0xA, 0xD, 0x2, 0x7],
    [0xC, 0x5, 0xE, 0x9]
]

# === Generate Inverse S-box ===
inv_s_box = [[0] * len(s_box[0]) for _ in range(len(s_box))]
for i in range(len(s_box)):
    for j in range(len(s_box[0])):
        val = s_box[i][j]
        row = val // len(s_box[0])
        col = val % len(s_box[0])
        if row < len(inv_s_box) and col < len(inv_s_box[0]):
            inv_s_box[row][col] = (i * len(s_box[0])) + j

# === Helper functions ===
def xor_bits(a, b):
    return ''.join(str(int(x)^int(y)) for x, y in zip(a, b))

def substitute(block, box):
    size = len(box)
    block_size = len(block)
    out = ""
    for i in range(0, block_size, 4):
        nibble = block[i:i+4]
        val = int(nibble, 2)
        row = val // size
        col = val % size
        sub_val = box[row][col]
        out += format(sub_val, '04b')
    return out

# === Encryption ===
def des_encrypt(plain_text, key, box=s_box):
    # Convert input to binary
    plain_bin = ''.join(format(ord(c), '08b') for c in plain_text)
    key_bin = ''.join(format(ord(c), '08b') for c in key)

    # XOR and substitute
    xored = xor_bits(plain_bin, key_bin[:len(plain_bin)])
    substituted = substitute(xored, box)

    return substituted

# === Decryption ===
def des_decrypt(cipher_bin, key, inv_box=inv_s_box):
    key_bin = ''.join(format(ord(c), '08b') for c in key)

    # Inverse substitute and XOR
    inv_sub = substitute(cipher_bin, inv_box)
    original_bin = xor_bits(inv_sub, key_bin[:len(cipher_bin)])

    # Convert back to text
    text = ''.join(chr(int(original_bin[i:i+8], 2)) for i in range(0, len(original_bin), 8))
    return text

# === Sample Usage ===
plain = "Hi"
key = "XY"  # Same length or longer than plain text
cipher = des_encrypt(plain, key)
print("Encrypted Binary:", cipher)

decrypted = des_decrypt(cipher, key)
print("Decrypted Text:", decrypted)