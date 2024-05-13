import input as ip
#import feistel as ft
#import keyschedule as ks

import random as rd

key = int(''.join(rd.choices(['0','1'], k=56)))
keyRotations = rd.choices([1,2], k=2)

def main() :
    for block in ip.handleInput() :
        encrypted = transform(block)
        decrypted = transform(encrypted)

        ip.handleOutput(block, decrypted)


def transform(block) :
    rBlock, lBlock = splitBlock(block)

    xBlock = rBlock ^ lBlock
    rBlock = rBlock << int(ip.blockLength/2)
    return rBlock | xBlock

def splitBlock(intg) :
    mask = int('1' * 32, 2)
    return [(intg & (mask << 32)) >> 32, intg & mask]

main()

#For Debugging
    #print("Block: " + bin(block)[2:])
    #print("R:     " + bin(rBlock)[2:])
    #print("L:     " + ("0" * 32) + bin(lBlock)[2:])
    #print(len(bin(rBlock)), len(bin(rBlock)))

        
    #print("")
    #print("Block: " + bin(block))
    #print("encrypted: " + bin(encrypted))
    #print("decrypted: " + bin(decrypted))
