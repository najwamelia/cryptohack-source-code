# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

from Crypto.Cipher import AES

import binascii
import hashlib
import requests
import sys

a = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ct_hex = a.json()["ciphertext"]

with open('pass_as_keys.txt', 'r') as f:
    for word in f:
        word = word.strip()
        att_key = hashlib.md5(word.encode()).hexdigest()

        ciphertext = bytes.fromhex(ct_hex)
        key = bytes.fromhex(att_key)
        cipher = AES.new(key, AES.MODE_ECB)

        try:
            decrypted = cipher.decrypt(ciphertext)
            r = binascii.unhexlify(decrypted.hex())
            if r.startswith('crypto{'.encode()):
                print("key is %s" % word)
                print(r.decode('utf-8'))
                sys.exit(0)

        except ValueError as o:
            continue

# flag = crypto{k3y5__r__n07__p455w0rdz?}
