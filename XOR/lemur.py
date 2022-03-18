# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

from PIL import Image, ImageChops

im1 = Image.open('D:/Sem 4/Kriptografi/Praktikum Cryptohack/XOR/lemur.png')
im2 = Image.open('D:/Sem 4/Kriptografi/Praktikum Cryptohack/XOR/flag.png')

im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3.show()
im3.save("D:/Sem 4/Kriptografi/Praktikum Cryptohack/XOR/solved.png")
