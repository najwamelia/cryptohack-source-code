# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

import binascii

str = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
conv = binascii.unhexlify(str)

key = bytes([conv[0] ^ ord('c')])

flag = ''
for char in range(len(conv)):
    flag += chr(conv[char] ^ ord(key))

print(flag)
