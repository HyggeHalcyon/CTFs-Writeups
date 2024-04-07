ENC = [0x9c, 0x96, 0xbd, 0xaf, 0x93, 0xc3, 0x94, 0x60, 0xa2, 0xd1, 0xc2, 0xcf, 0x9c, 0xa3, 0xa6, 0x68, 0x94, 0xc1, 0xd7, 0xac, 0x96, 0x93, 0x93, 0xd6, 0xa8, 0x9f, 0xd2, 0x94, 0xa7, 0xd6, 0x8f, 0xa0, 0xa3, 0xa1, 0xa3, 0x56, 0x9e]
FLAG = ['H'] # known flag HTB{

def main():
    for i in range(0, len(ENC)):
        tmp = chr( ENC[i] - ord(FLAG[i]) )
        FLAG.append(tmp)

    print(''.join(FLAG))

if __name__ == '__main__':
    main()