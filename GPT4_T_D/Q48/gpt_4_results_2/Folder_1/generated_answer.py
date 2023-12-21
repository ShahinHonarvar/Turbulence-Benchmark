
def return_binary_or_hexa(tup):
    a = tup[17]
    b = tup[88]
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(tup[17:89]))
    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]
