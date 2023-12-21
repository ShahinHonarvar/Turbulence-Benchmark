
def return_binary_or_hexa(tup):
    a = tup[73]
    b = tup[84]
    sum1 = sum(set(range(a + 1, b)) - set(tup[73:85]))
    if sum1 % 2 == 0:
        return hex(sum1)[2:]
    else:
        return bin(sum1)[2:]
    return ''
