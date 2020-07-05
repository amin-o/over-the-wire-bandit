#!/usr/bin/env python
from pwn import *

shell = ssh('bandit3', 'bandit.labs.overthewire.org', password='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK', port=2220)

password = shell['cat inhere/.hidden'].decode()

print(password)



 