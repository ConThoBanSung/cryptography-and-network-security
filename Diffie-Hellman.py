from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Bên A tạo khóa Diffie-Hellman
parameters = dh.generate_parameters(generator=2, key_size=2048)
private_key_A = parameters.generate_private_key()
public_key_A = private_key_A.public_key()

# Bên B tạo khóa Diffie-Hellman
private_key_B = parameters.generate_private_key()
public_key_B = private_key_B.public_key()

# Bên A và B trao đổi khóa công khai để tạo khóa chung
shared_key_A = private_key_A.exchange(public_key_B)
shared_key_B = private_key_B.exchange(public_key_A)

print("Khóa chung được bên A tạo:", shared_key_A)
print("Khóa chung được bên B tạo:", shared_key_B)

# Cả hai bên đều có cùng khóa chung
assert shared_key_A == shared_key_B
