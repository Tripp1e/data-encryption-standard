def checkError(input, amount) :
    modulo = len(input) % amount
    if modulo != 0 :
        raise ValueError("The Length of Input does not match the amount. Got: " + str(modulo))

def toBinary(input) :
    return [format(ord(char), 'b') for char in input]

def missingTo(input, amount) :
    return amount - (len(input) % amount)

def groupArray(input, amount) :
    checkError(input, amount)
    return [input[i:i+amount] for i in range(0, len(input), amount)]

def splitArray(input, amount) :
    checkError(input, amount)
    amount = int(len(input) / amount)
    return [input[i:i+amount] for i in range(0, len(input), amount)]

def getMissingBits(input, amount) :
    binStrings = []
    
    for char in input :
        missingBits = missingTo(char, amount)
        binStrings.append(("0" * missingBits) + char)
    return binStrings
