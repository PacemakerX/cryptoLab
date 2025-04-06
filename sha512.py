import hashlib

# Get user input
text = input("Enter text to hash using SHA-512: ")

# Encode and hash
hash_object = hashlib.sha512(text.encode())
hash_hex = hash_object.hexdigest()

# Output the hash
print("SHA-512 Hash:")
print(hash_hex)
