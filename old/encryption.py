import random
import string

blockSize = 64

key = ''.join(random.choices(["0","1"], k=56))
#True = 1 , False = 2
shiftRight = []
shiftLeft = []

# Split String into length long parts.
def split(string, length) :
    length = int(length)
    return [string[i:i+length] for i in range(0, len(string), length)]

# Convert String to Binary and return a list of blockSize long parts.
def toBinary(string) :
    binStrings = []
    binString = lambda : ''.join(binStrings)
    
    for char in string : 
        binStrings.append(format(ord(char), 'b'))
    
    for item in binStrings :
        x = ("0" * (8 - len(item))) + item

    binStrings.append("0" * (blockSize - (len(binString()) % blockSize)))

    return split(binString(), blockSize) 

#Apply the feistel function
def feistel(rblock) :
    if len(rblock) != 32 :
        raise ValueError("RBlocks must have a size of 32")
    
    rblock = expansion(rblock)
    keySchedule(key)


    return ""

#Expansion for the Feistel function
def expansion(rblock) :
    blocks = split(rblock, 4)
    expandedBlocks = [""] * len(blocks)

    maxIndex = len(blocks) - 1

    for i in range(maxIndex) :
        prevBlock = blocks[i-1]
        nextBlock = blocks[i+1]
        
        if i == 0 :
            prevBlock = blocks[maxIndex]
        if i == maxIndex:
            nextBlock = blocks[0]

        expandedBlocks[i] = prevBlock[3] + blocks[i] + nextBlock[0]

    return expandedBlocks

def keySchedule(half) :
    subkeys = []
    halfs = split(half, len(key)/2)
    print("this is being run")
    for i in range(16) :
        print("Halfs: " + str(halfs))
        leftRotate(halfs[0], shiftRight)
        leftRotate(halfs[1], shiftLeft)

        right = removeBits(half[0], 4)
        left = removeBits(half[1], 4)
        
        subkeys.append([''.join([right,left])])
    
    print(subkeys)

    

def leftRotate(bitsArray, right) :
    for bits in bitsArray :
        amount = random.choices([1,2])[0]
        shiftRight.append(amount) if right else shiftLeft.append(amount)
        bits = bits[amount:len(bits)-1] + bits[0:amount-1]

    return bitsArray

def removeBits(bits, amount) :
    bits = bits[0:len(bits)-(amount+1)]
    return bits

def main() :
    message = input()
    binMessage = toBinary(message)

    for block in binMessage :
        if len(block) != blockSize :
            raise ValueError("All Blocks must have a size of 64")
               
        block = split(block, int(blockSize/2))

        rblock = block[0]
        lblock = block[1]
        
        feistel(rblock)


main()
