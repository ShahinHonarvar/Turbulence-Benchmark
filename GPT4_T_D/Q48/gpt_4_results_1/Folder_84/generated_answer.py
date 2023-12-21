
def return_binary_or_hexa(nTuple):
    a = nTuple[32]
    b = nTuple[44]
    sumVals = sum(num for num in range(a+1, b) if num not in nTuple[32:45])
    if sumVals == 0:
        return ''
    elif sumVals%2 == 0:
        return hex(sumVals)[2:].upper()
    else:
        return bin(sumVals)[2:]
