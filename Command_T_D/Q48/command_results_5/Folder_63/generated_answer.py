
def return_binary_or_hexa(tup):
    a, b = tup[81], tup[86]
    diff = b - a - 1
    if diff % 2 == 1:
        return '0b' + bin(diff)[2:].zfill(8)
    else:
        return '0x' + hex(diff)[2:].zfill(4)
