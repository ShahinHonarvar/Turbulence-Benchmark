
def return_binary_or_hexa(t):
    a = t[55]
    b = t[84]
    missing_nums_sum = sum(set(range(a+1, b)) - set(t[55:85]))
    if missing_nums_sum % 2:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
