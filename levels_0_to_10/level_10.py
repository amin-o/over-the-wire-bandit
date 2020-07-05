#!/usr/bin/env python
from pwn import *
import base64

shell = ssh('bandit10', 'bandit.labs.overthewire.org', password='truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk', port=2220)

data = shell['cat data.txt'].decode()
decoded_data = base64.b64decode(data).decode().split()

print(decoded_data[3])
 




