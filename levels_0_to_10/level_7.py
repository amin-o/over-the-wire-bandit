#!/usr/bin/env python
from pwn import *

shell = ssh('bandit7', 'bandit.labs.overthewire.org', password='HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs', port=2220)

data = shell['cat data.txt | grep millionth'].decode()
data = data.split()

print(data[1])
 




