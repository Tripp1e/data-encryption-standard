blockLength = 64
charLength = 8
charpBlock = int(blockLength/charLength)

message = ""

def handleInput() :
    message = "Hello World!"
    binMessage = binOf(message)
    return blocksOf(binMessage)

def handleOutput(unencrypted, decrypted) :
    if unencrypted == decrypted :
        print("Success!")
    else :
        print("Failure!")
    
def binOf(stri) :
    lst = [ord(char) for char in stri]
    lst = [bin(intg)[2:] for intg in lst]
    lst = [missingDigits(bin, charLength) + bin for bin in lst]
    lst = [''.join(lst[i:i+charpBlock]) for i in range(0, len(lst), charpBlock)]
    return int(''.join(lst),2)

def blocksOf(intg) :
    bstr = bin(intg)[2:]
    bstr = missingDigits(bstr, 64) + bstr
    bstr = len(bstr)

    mask = int('1' * blockLength, 2)
    return [(intg & (mask << i)) >> i for i in range(0, bstr, blockLength)]

def missingDigits(a, b) :
    return "0" * (b - (len(a) % b))
