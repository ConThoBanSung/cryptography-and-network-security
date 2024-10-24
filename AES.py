from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Khóa bí mật (cần giữ an toàn)
key = get_random_bytes(16)  # AES-128: Khóa 16 bytes

# Dữ liệu cần mã hóa
data = b"Hello, this is a secret message!"
print("Dữ liệu gốc:", data)

# Mã hóa dữ liệu
cipher = AES.new(key, AES.MODE_CBC)  # Sử dụng AES trong chế độ CBC
ciphertext = cipher.encrypt(pad(data, AES.block_size))
print("Dữ liệu mã hóa:", ciphertext)

# Lưu lại IV để giải mã
iv = cipher.iv

# Giải mã dữ liệu
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print("Dữ liệu sau giải mã:", plaintext)
