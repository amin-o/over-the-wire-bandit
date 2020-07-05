#!/usr/bin/env python
from pwn import *

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)

password = shell['cat readme'].decode()

print(password)
