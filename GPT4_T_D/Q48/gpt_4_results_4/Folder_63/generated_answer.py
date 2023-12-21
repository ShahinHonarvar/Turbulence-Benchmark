
def return_binary_or_hexa(tup):
    a = tup[81]
    b = tup[86]
    excluded_nums = set(range(a + 1, b)) - set(tup[81:87])
    sum_excluded = sum(excluded_nums)
    if sum_excluded == 0:
        return ''
    elif sum_excluded % 2 == 0:
        return hex(sum_excluded)[2:].upper()
    else:
        return bin(sum_excluded)[2:]
