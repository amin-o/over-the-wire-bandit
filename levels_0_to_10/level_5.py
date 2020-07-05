#!/usr/bin/env python
from pwn import *

shell = ssh('bandit5', 'bandit.labs.overthewire.org', password='koReBOKuIDDepwhWk7jZC0RTdopnAYKh', port=2220)

files = shell['find . -type f -size 1033c ! -executable'].decode()
files = files.splitlines()
 
for x in files:

    print('\nExtracting data from ' + x)
    print(shell['cat ' + x].decode())




