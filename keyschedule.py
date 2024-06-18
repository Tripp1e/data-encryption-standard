import random as rd
import lookuptable

rots = []
mask28 = int('1' * 28, 2)
key = rd.randint(0, 2**64)

def getSubKeys() :
    subKeys = []
    shffl = permutatedChoice(key, True)

    left, right = splitKey(shffl)
    
    for  i in range(16):
        rot = rd.choices([1, 2], k=2)
        rotL, rotR = rot
        rots.append(rot)
        
        left = rotate(left, rotL)
        right = rotate(right, rotR)
        
        subKeys.append(permutatedChoice(((left << 28) | right), False))
    return subKeys

def permutatedChoice(key, pc1) :
    key = bin(key)[2:]
    shffl = ""
    table = lookuptable.PC1 if pc1 else lookuptable.PC2
    for i in range(len(table)) :
        index = table[i]
        try :
            shffl = shffl + key[index - 1]
        except :
            shffl = shffl + '0'
    return int(shffl, 2)

def rotate(n, k) :
    b = n >> (28-k)
    return (b | (n << k)) & mask28

def splitKey(key) :
    return key >> 28, key & mask28

print(getSubKeys())
