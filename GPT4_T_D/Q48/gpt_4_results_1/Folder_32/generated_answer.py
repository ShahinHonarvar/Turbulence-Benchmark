
def return_binary_or_hexa(tup):
    a, b = tup[86], tup[90]
    total_sum = sum(set(range(a + 1, b)) - set(tup[86:91]))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
