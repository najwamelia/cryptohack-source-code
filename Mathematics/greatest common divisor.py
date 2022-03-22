# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

def gcd(a, b):
    while b > 0:
        q, remainder = divmod(a, b)
        a, b = b, remainder
    return a

print(gcd(66528, 52920))

# cara lain
#import math
#print(math.gcd(66528, 52920))
