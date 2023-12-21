
def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    missing_nums_sum = sum(set(range(a+1, b)) - set(tup[1:8]))
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:].upper()
    else:
        return bin(missing_nums_sum)[2:]
