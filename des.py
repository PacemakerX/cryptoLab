def string_to_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

def binary_to_string(b):
    chars = [b[i:i+8] for i in range(0, len(b), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def xor(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

def des_encrypt(plain_text, key):
    binary_plain = string_to_binary(plain_text)
    binary_key = string_to_binary(key)

    # For simplicity, make key same length as plain text
    binary_key = (binary_key * ((len(binary_plain) // len(binary_key)) + 1))[:len(binary_plain)]

    cipher_binary = xor(binary_plain, binary_key)
    return cipher_binary

def des_decrypt(cipher_binary, key):
    binary_key = string_to_binary(key)
    binary_key = (binary_key * ((len(cipher_binary) // len(binary_key)) + 1))[:len(cipher_binary)]

    decrypted_binary = xor(cipher_binary, binary_key)
    return binary_to_string(decrypted_binary)

# === Example Usage ===
plain = input("Enter plaintext: ")
key = input("Enter key: ")

cipher = des_encrypt(plain, key)
print("Encrypted (binary):", cipher)

decrypted = des_decrypt(cipher, key)
print("Decrypted:", decrypted)
