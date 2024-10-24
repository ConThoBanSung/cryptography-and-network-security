from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Tạo cặp khóa RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Thông điệp cần ký
message = b"Message to be signed"
print("Thông điệp:", message)

# Băm thông điệp
hash_message = SHA256.new(message)

# Ký thông điệp với khóa riêng
signature = pkcs1_15.new(key).sign(hash_message)
print("Chữ ký số:", signature)

# Xác thực chữ ký với khóa công khai
try:
    pkcs1_15.new(key.publickey()).verify(hash_message, signature)
    print("Chữ ký hợp lệ")
except (ValueError, TypeError):
    print("Chữ ký không hợp lệ")
