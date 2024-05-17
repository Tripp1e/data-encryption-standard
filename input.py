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
        	text = chr(char) + text
        print(text)
    else :
        print("Failure!")

def binOf(stri):
    bin = 0
    for char in stri:
        bin = (bin << charLength) | ord(char)
    return bin

def blocksOf(intg, leng) :
    mask = (1 << leng) - 1
    blocks =	[]
    while intg :
    	blocks.append(intg & mask)
    	intg >>= leng
    return blocks