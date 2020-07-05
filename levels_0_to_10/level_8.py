#!/usr/bin/env python
from pwn import *

shell = ssh('bandit8', 'bandit.labs.overthewire.org', password='cvX2JJa4CFALtqS87jk27qwqGhBM9plV', port=2220)

data = shell['sort data.txt | uniq -u '].decode()
 
print(data)
 




