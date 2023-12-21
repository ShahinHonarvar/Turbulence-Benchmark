
def return_binary_or_hexa(tup):
    a = tup[81]
    b = tup[86]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(tup[81:87]))
    if missing_nums_sum % 2 != 0:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
