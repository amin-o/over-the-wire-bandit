#!/usr/bin/env python
from pwn import *

shell = ssh('bandit9', 'bandit.labs.overthewire.org', password='UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR', port=2220)

data = shell['strings data.txt | grep ='].decode()
data = data.split()
 
print(data[15])
 




