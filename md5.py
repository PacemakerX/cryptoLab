import hashlib

text = input("Enter string to hash with MD5: ")
result = hashlib.md5(text.encode())
print("MD5 Hash:", result.hexdigest())
