# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

p = 26513
q = 32321

if p < q:
    p, q = q, p  # Reverse urutan

a1, a2 = p, q
b1, b2 = 1, 0
c1, c2 = 0, 1

while a2 > 0:
    n, a = divmod(a1, a2)  
    a1, a2 = a2, a
    
    b1, b2 = b2, b1 - n * b2
    c1, c2 = c2, c1 - n * c2

print(f"GCD:{a1}, u:{c1}, v:{b1}")