enc = [0xD2,0x95,0xC2,0x70,0xA4,0x53,0xD5,0x4A,0x3D,0xC0,0x9A,0x3C,0x62,0x0D,0xA7,0x41,0xEA,0x2A,0x3C,0x85,0x73,0xC6,0xAC,0x47,0xEE,0x87,0x0D,0x64,0xB8,0x5E,0xA9,0x5A,0x0D,0x47,0x8D,0x3B,0x8A,0x58,0x8A,0x00,0x05,0xDA,0x81,0x44,0xAB,0x2E,0x96,0x93,0x6E,0x43,0x56,0x1B,0x9D,0x51,0x89,0x60,0x29,0xAE,0x09,0x54,0x4E,0x7F,0xD3,0xC0,0x82,0xE8,0x0D,0xA3,0x33,0x52,0xAC,0x20,0xBD]

rand_key = [
    0x91,
    0xdf,
    0xf0,
    0x40,
    0x96,
    0x60,
    0xae,
    0x3e,
    0x5f,
    0xa8,
    0xc5,
    0x55,
    0x3d,
    0x7f,
    0xc6,
    0x2f,
    0xb5,
    0x45,
    0x49,
    0xf1,
    0x2c,
    0xa9,
    0xca,
    0x18,
    0x87,
    0xe3,
    0x68,
    0x05,
    0xcb,
    0x01,
    0xc0,
    0x3e,
    0x66,
    0x18,
    0xe4,
    0x5d,
    0xd5,
    0x21,
    0xe5,
    0x75,
    0x5a,
    0xbd,
    0xf4,
    0x3d,
    0xd8,
    0x71,
    0xfa,
    0xf6,
    0x0f,
    0x31,
    0x38,
    0x7e,
    0xf9,
    0x0e,
    0xe8,
    0x0e,
    0x50,
    0xda,
    0x61,
    0x3d,
    0x20,
    0x18,
    0x8c,
    0xa6,
    0xf0,
    0x87,
    0x60,
    0xfc,
    0x47,
    0x3a,
    0xc5,
    0x53,
    0xc0,
]

flag = []

for i in range(0, len(rand_key)):
    flag.append( chr(enc[i] ^ rand_key[i]) )

print(''.join(flag))