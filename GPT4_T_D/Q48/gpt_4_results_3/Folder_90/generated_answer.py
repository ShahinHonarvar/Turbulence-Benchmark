
def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[90]
    total_sum = sum(range(a + 1, b)) - sum(tup[61:90])
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
