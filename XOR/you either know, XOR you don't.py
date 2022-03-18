# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

str = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

flag_format = b"crypto{"
key = [o1 ^ o2
       for (o1, o2) in zip(str, flag_format)] + [ord("y")]

flag = []
key_len = len(key)
for i in range(len(str)):
    flag.append(str[i] ^ key[i % key_len])
flag = "".join(chr(o) for o in flag)

print(flag)
