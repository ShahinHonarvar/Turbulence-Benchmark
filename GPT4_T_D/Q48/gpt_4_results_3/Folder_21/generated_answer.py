
def return_binary_or_hexa(tup):
    a = tup[15]
    b = tup[57]
    missing_nums_sum = sum(set(range(a+1, b)) - set(tup[15:58]))
    if missing_nums_sum == 0:
        return ""
    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:]
    else:
        return bin(missing_nums_sum)[2:]
