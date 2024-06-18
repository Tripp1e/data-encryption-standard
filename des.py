import input as ip
#import feistel as ft
import keyschedule as ks
import random as rd


mask32 = int('1'* 32, 2)

def main() :
    
    ks.getSubKeys()

    for block in ip.handleInput() :
        print("Unencrypted: " + str(block))
        encrypted = transform(block)
        print("Enrypted: "+  str(encrypted))
        decrypted = transform(encrypted)
        print("Decrypted: " + str(decrypted))

        ip.handleOutput(block, decrypted)
        
def transform(block) :
    rBlock, lBlock = splitBlock(block)

    xBlock = rBlock ^ lBlock
    rBlock = rBlock << 32
    return rBlock | xBlock

def splitBlock(intg) :
    return [(intg >> 32) & mask32, intg & mask32]

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
