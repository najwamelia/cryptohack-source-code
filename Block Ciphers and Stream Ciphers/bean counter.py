# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

import requests
from Crypto.Util.strxor import strxor

link ='http://aes.cryptohack.org/bean_counter/encrypt/'
response = requests.get(link)

msg = bytes.fromhex(response.json()['encrypted'])
top = bytes.fromhex('89504e470d0a1a0a0000000d49484452')

n = strxor(top, msg[:16])
pt = b''
for i in range(0,len(msg),16):
	block = msg[i:i+16]
	pt+=strxor(block, n[0:len(block)])

f=open('bcflag.png','wb').write(pt)

# flag = crypto{hex_bytes_beans}
