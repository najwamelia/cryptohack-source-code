# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

#!/usr/bin/env python3

import requests

ct_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt_flag/').json()
ct = ct_hex['ct']
print(ct)

n = ct[:16*2]
print(n)
ct = ct[32:]
print(ct)

pt_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt/'+ct+'/'+n+'/').json()
pt = pt_hex['ct']
print(pt)

flag = bytes.fromhex(pt)
print(flag)

# flag = crypto{0fb_15_5ymm37r1c4l_!!!11!}
