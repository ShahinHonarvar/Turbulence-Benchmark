
def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    missing_nums = set(range(a + 1, b)) - set(tup[276:871])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
