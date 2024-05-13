from des import message
from des import key

def feistel(rblock) :
    if len(rblock) != 32 :
        raise ValueError("rblock is not 32 bits.")
    rblock = expand(rblock)
    subKeys = keyschedule()

def expand(block) :
    original = split(block, 4)
    
    expanded = []

    for i in range(len(original)) :
        a = 0 if i == len(original) else i+1
        current = original[i-1][3] + original[i] + original[a][0]
        expanded.append(current)

    return expanded

def split(block, length) :
    mask = int('1' * amount, 2)
    return [block & (mask << i*amount) for i in range(int(amount/len(block)))]

def keyschedule() :
    if len(key) != 56 :
        raise ValueError("Key has to be 64 Bits")
    rkey, lkey = split(key, 28)
    
    for i in range(16),
        rkey << 2
        lkey << 2
    

    return
