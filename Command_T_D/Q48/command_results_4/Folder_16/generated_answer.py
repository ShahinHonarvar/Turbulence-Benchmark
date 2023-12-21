
def return_binary_or_hexa(tup):
    a, b = tup[90], tup[97]
    diff = b - a - 1
    if diff & 1:
        return "0b" + bin(diff)[2:]
    else:
        return "0x" + hex(diff)[2:]
