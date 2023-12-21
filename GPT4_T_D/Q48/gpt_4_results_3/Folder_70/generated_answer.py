
def return_binary_or_hexa(tup):
    a = tup[43]
    b = tup[70]
    missing_nums = set(range(a+1, b)) - set(tup[43:70])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]
