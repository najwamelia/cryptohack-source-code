# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

from tkinter import N
from Crypto.Cipher import AES
import requests

def xor(m, n):
	m = bytes.fromhex(m)
	n = bytes.fromhex(n)
	return bytes(i ^ j for i, j in zip(m, n))

def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    cipher = AES.new(KEY, AES.MODE_ECB)
    
    try:
        decrypted = cipher.decrypt(ciphertext)
        
    except ValueError as o:
        return {"error": str(o)}

    return {"plaintext": decrypted.hex()}
        
cipher = requests.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
cipher = cipher.json()['ciphertext']

a = cipher[:32]
cipher1 = cipher[32:64]
cipher2 = cipher[64:96]
decrypt2 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher2 + '/')
decrypt2 = decrypt2.json()['plaintext']
decrypt2 = xor(decrypt2,cipher1)
decrypt1 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher1 + '/')
decrypt1 = decrypt1.json()['plaintext']
decrypt1 = xor(decrypt1, a)

print(decrypt1 + decrypt2)

# flag  crypto{3cb_5uck5_4v01d_17_!!!!!}
