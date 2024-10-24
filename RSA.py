from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Tạo cặp khóa RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Lưu trữ và hiển thị khóa
with open("private.pem", "wb") as f:
    f.write(private_key)

with open("public.pem", "wb") as f:
    f.write(public_key)

# Mã hóa với khóa công khai
message = b'This is a secret message!'
print("Dữ liệu gốc:", message)
public_key = RSA.import_key(open("public.pem").read())
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_message = cipher_rsa.encrypt(message)
print("Dữ liệu mã hóa:", encrypted_message)

# Giải mã với khóa riêng tư
private_key = RSA.import_key(open("private.pem").read())
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted_message = cipher_rsa.decrypt(encrypted_message)
print("Dữ liệu sau giải mã:", decrypted_message)
