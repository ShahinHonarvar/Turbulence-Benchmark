
def return_binary_or_hexa(tup):
    a = tup[51]
    b = tup[76]
    missing_nums = set(range(a + 1, b)) - set(tup[51:77])
    summed = sum(missing_nums)
    if summed == 0:
        return ''
    elif summed % 2 == 1:
        return bin(summed)[2:]
    else:
        return hex(summed)[2:].upper()
