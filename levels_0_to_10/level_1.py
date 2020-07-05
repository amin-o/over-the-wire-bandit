#!/usr/bin/env python
from pwn import *

shell = ssh('bandit1', 'bandit.labs.overthewire.org', password='boJ9jbbUNNfktd78OOpsqOltutMc3MY1', port=2220)

password = shell['cat ./-'].decode()

print(password)

