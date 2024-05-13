import utils
import random

blockLength = 64
charLength = 8
charPerBlock = int(blockLength/charLength)

key = ''.join(random.choices([0,1], k=56))


def main() :
    print("The Key is" +  str(key))
    message = "Hello World!"
    binChars = getCharsInBinary(message)
    blocks = utils.groupArray(binChars, charPerBlock)
    for block in blocks :
        encrypt(block)

def genSubKeys() :


def getCharsInBinary(string) :
    binString = utils.toBinary(string)
    missingBlocks = utils.missingTo(binString, charPerBlock)
    
    for i in range(missingBlocks) :
        binString.append(0)
    
    return binString

def encrypt(block) :
    blocks = utils.splitArray(block, 2)
    rblock = blocks[0]
    
    feistel(rblock)
    
    return

def feistel(bits) :
    bits = expansion(bits)


def expansion(rBlock) :
    rBlock = utils.getMissingBits(rBlock)
    
    originalBits = []
    for char in rBlock :
        originalBits = originalBits + utils.groupArray(char, 4)

    expandedBits = [""] * len(originalBits)
    for i in range(len(originalBits)) :
        a = 0 if i == len(originalBits) else i
        expandedBits[i] = originalBits[i-1][3] + originalBits[i] + originalBits[a][0]

    return expandedBits

main()
