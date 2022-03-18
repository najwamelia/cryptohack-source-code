# Najwa Amelia Qorry 'Aina - 5027201001
#!/usr/bin/env python3

import base64

ords = bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
conv = base64.b64encode(ords)

print(conv)
