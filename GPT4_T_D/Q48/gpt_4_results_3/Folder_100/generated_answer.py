
def return_binary_or_hexa(tup):
    a, b = tup[44], tup[78]
    sum_absent = sum(set(range(a + 1, b)) - set(tup[44:79]))
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:].upper()
