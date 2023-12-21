
def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[200]
    sum_not_in_range = sum(set(range(a + 1, b)) - set(tup[20:200]))
    if sum_not_in_range == 0:
        return ""
    elif sum_not_in_range % 2 == 1:
        return bin(sum_not_in_range)[2:]
    else:
        return hex(sum_not_in_range)[2:].upper()
