import des

def getsubKey() :
    #Key is generated with 56 bits and PC 1 is just halving
    #for simplicity reasons.
    halfs = splitKey(des.key)
    for i in range(len(halfs)) :
        rot = des.keyRotations[i]
        bits = bin(halfs[i])[2:rot]
        print("Bits" + bits)
        rest = bin(halfs[i])[2:rot + 4:] + bits
        print("Rest" + rest)
        halfs[i] = int(rest, 2)
    return ''.join(halfs)

def splitKey(key) :
    mask = int('1' * 28, 2)
    return [(key & (mask << 28)) >> 28, key & mask]
getsubKey()
