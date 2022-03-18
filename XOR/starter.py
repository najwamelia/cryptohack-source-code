# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

str = 'label'
flag = ''

for char in str:
    flag = flag + chr(ord(char) ^ 13)

print(flag)
