
def return_binary_or_hexa(tup):
    a = tup[15]
    b = tup[57]
    sum_values = sum(set(range(a + 1, b)) - set(tup[15:58]))
    if sum_values == 0:
        return ""
    elif sum_values % 2 == 0:
        return hex(sum_values)[2:].upper()
    else:
        return bin(sum_values)[2:]
