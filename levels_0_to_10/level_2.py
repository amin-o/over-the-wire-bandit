#!/usr/bin/env python
from pwn import *

shell = ssh('bandit2', 'bandit.labs.overthewire.org', password='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9', port=2220)

password = shell['cat ./spaces\ in\ this\ filename'].decode()

print(password)

