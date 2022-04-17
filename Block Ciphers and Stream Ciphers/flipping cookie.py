# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

from datetime import datetime, timedelta
import requests

def flippp(cokieee, pt):
    start = pt.find(b'admin=False')
    cokieee = bytes.fromhex(cokieee)
    n = [0xff] * 16
    ctfalse = list(cokieee)
    zonk = b';admin=True;'
    for i in range(len(zonk)):
       ctfalse[start+i] = pt[start+i] ^ cokieee[start+i] ^ zonk[i]
       n[start+i] = pt[start+i] ^ cokieee[start+i] ^ zonk[i]
    ctfalse = bytes(ctfalse).hex()
    n = bytes(n).hex()
    return ctfalse, n

def req_cokieee():
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie/")
    return r.json()["cookie"]

def req_adm(cokieee, n):
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/check_admin/{}/{}/".format(cokieee, n))
    return r.json()

def printblock(hex, size):
   for i in range(0, len(hex), size):
       print(hex[i:i+size], ' ', end='')
   print()

expire = (datetime.today() + timedelta(days=1)).strftime("%S")
pt = f"admin=False;expiry={expire}".encode()
cokieee = req_cokieee()
cokieee, n = flippp(cokieee, pt)

print(req_adm(cokieee, n))

# flag = crypto{4u7h3n71c4710n_15_3553n714l}
