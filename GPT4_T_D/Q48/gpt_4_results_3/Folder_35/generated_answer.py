
def return_binary_or_hexa(tup):
    a = tup[77]
    b = tup[84]
    sum_int = sum(set(range(a + 1, b)) - set(tup[77:84]))
    if sum_int % 2 == 0:
        return hex(sum_int)[2:]
    else:
        return bin(sum_int)[2:]
