blockLength = 64
charLength = 8
charpBlock = int(blockLength/charLength)

message = ""

def handleInput() :
    message = input()
    binMessage = binOf(message)
    return blocksOf(binMessage, blockLength)

def handleOutput(unencrypted, decrypted) :
    if unencrypted == decrypted :
        print("Success!")
        text = ""
        for char in blocksOf(decrypted, charLength) :
        	print(char)
        	text = chr(char) + text
        print(text)
    else :
        print("Failure!")
    
def binOf(stri) :
    #return [(bin << charLength) | ord(stri[i]) for i in range(len(stri))]
    bin = 0
    for i in range(len(stri)) :
        bin = (bin << charLength) | ord(stri[i])
    return bin

def blocksOf(intg, leng) :
    bits = 0
    while 2 ** bits < intg :
    	bits += 1
    mask = int('1' * leng, 2)
    return [(intg & (mask << i)) >> i for i in range(0, bits, leng)]