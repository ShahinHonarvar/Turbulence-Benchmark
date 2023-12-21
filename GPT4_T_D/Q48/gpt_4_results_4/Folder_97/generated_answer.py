
def return_binary_or_hexa(tup):
    a = tup[34]
    b = tup[69]
    s = set(tup[34:70])
    missing = [x for x in range(a + 1, b) if x not in s]
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
