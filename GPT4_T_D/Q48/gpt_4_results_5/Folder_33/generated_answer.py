
def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    total_sum = sum(set(range(a + 1, b)) - set(tup[13:36]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
