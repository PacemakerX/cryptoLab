# Simple S-Box
s_box = {
    '0': 'E', '1': '4', '2': 'D', '3': '1',
    '4': '2', '5': 'F', '6': 'B', '7': '8',
    '8': '3', '9': 'A', 'A': '6', 'B': 'C',
    'C': '5', 'D': '9', 'E': '0', 'F': '7'
}

inv_s_box = {v: k for k, v in s_box.items()}

def substitute(block):
    return ''.join(s_box.get(c.upper(), c) for c in block)

def inverse_substitute(block):
    return ''.join(inv_s_box.get(c.upper(), c) for c in block)

def xor_hex(a, b):
    return ''.join(hex(int(x, 16) ^ int(y, 16))[2:] for x, y in zip(a, b))

def aes_encrypt(plain_hex, key_hex):
    xored = xor_hex(plain_hex, key_hex)
    substituted = substitute(xored)
    return substituted

def aes_decrypt(cipher_hex, key_hex):
    inv_sub = inverse_substitute(cipher_hex)
    decrypted = xor_hex(inv_sub, key_hex)
    return decrypted

# === Example Usage ===
plain_text = input("Enter 8 hex chars (e.g. 1a2b3c4d): ").lower()
key = input("Enter 8 hex chars key: ").lower()

cipher = aes_encrypt(plain_text, key)
print("Encrypted:", cipher)

decrypted = aes_decrypt(cipher, key)
print("Decrypted:", decrypted)
