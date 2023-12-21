
def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    missing_nums_sum = sum(set(range(a+1, b)) - set(t[34:69]))
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:].upper()
    else:
        return bin(missing_nums_sum)[2:]
