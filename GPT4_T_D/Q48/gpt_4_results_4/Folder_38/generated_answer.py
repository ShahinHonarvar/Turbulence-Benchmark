
def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[85]
    missing_nums = set(range(a + 1, b)) - set(tup[36:86])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ""
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
