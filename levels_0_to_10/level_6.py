#!/usr/bin/env python
from pwn import *

shell = ssh('bandit6', 'bandit.labs.overthewire.org', password='DXjZPULLxYr17uwoI01bNLQbtFemEgo7', port=2220)

files = shell['find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null'].decode()
files = files.splitlines()
 
for x in files:

    print('\nExtracting data from ' + x)
    print(shell['cat ' + x].decode())




