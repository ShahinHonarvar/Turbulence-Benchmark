
def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    sum_value = sum(set(range(a+1, b)) - set(tup[86:90]))
    if sum_value % 2 != 0:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].upper()
