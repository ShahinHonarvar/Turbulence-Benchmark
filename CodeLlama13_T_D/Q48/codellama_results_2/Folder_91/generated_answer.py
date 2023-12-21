
def return_binary_or_hexadecimal(myTuple):
    result = ""
    for i in range(len(myTuple)):
        if myTuple[i+1] - myTuple[i] == 1:
            result += "0b" + bin(myTuple[i])[2:]
        else:
            result += hex(myTuple[i])[2:].upper()
    return result.lstrip("0")
