
def return_binary_or_hexa(tup):
    a, b = tup[17], tup[88]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(tup[17:89]))

    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
