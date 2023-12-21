
def return_binary_or_hexa(tup):
    a, b = tup[11], tup[76]
    not_present = set(range(a + 1, b)) - set(tup[11:77])
    sum_not_present = sum(not_present)
    if not not_present:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()
