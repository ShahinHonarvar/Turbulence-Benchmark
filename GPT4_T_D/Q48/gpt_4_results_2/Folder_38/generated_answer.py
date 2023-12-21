
def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[85]
    missing_integers = set(range(a + 1, b)) - set(tup[36:86])
    sum_miss_int = sum(missing_integers)
    if sum_miss_int == 0:
        return ''
    elif sum_miss_int % 2 == 1:
        return bin(sum_miss_int)[2:]
    else:
        return hex(sum_miss_int)[2:].upper()
