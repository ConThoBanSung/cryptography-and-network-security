import hashlib

# Dữ liệu cần băm
data = "This is some data to hash".encode()

# Tạo giá trị băm SHA-256
hash_object = hashlib.sha256(data)
hash_value = hash_object.hexdigest()

print("Dữ liệu gốc:", data)
print("Giá trị băm SHA-256:", hash_value)
