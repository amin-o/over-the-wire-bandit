#!/usr/bin/env python
from pwn import *

shell = ssh('bandit4', 'bandit.labs.overthewire.org', password='pIwrPrtPN36QITSp3EQaw936yaFoFgAB', port=2220)

file = shell['cd inhere ; file ./-* | grep ASCII | cut -c1-9'].decode()
password = shell['cat inhere/' + file].decode()

print(password)



