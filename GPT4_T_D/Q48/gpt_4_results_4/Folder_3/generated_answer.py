
def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    missing_nums_sum = sum(set(range(a+1, b)) - set(t[56:88]))
    if missing_nums_sum == 0:
        return ""
    elif missing_nums_sum % 2 != 0:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
