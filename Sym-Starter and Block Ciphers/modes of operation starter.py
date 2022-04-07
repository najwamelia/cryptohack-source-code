# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

# cipherteks dari encrypted flag
a = requests.get(f"{BASE_URL}/encrypt_flag")
data = a.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

# 2) send the ciphertext to the decrypt function
a = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = a.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

# 3) konversi hex ke ascii
print("flag", bytearray.fromhex(plaintext).decode())

# flag = crypto{bl0ck_c1ph3r5_4r3_f457_!}
