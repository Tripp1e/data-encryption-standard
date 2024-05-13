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
    bin = 0
    for i in range(len(stri)) :
        bin = (bin << charLength) | ord(stri[i])
    return bin

def blocksOf(intg) :
    bstr = bin(intg)[2:]
    bstr = len(missingDigits(bstr, 64) + bstr)
    mask = int('1' * blockLength, 2)
    return [(intg & (mask << i)) >> i for i in range(0, bstr, blockLength)]

def missingDigits(a, b) :
    return "0" * (b - (len(a) % b))

binOf("Hellooo")
