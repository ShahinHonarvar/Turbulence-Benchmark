
def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    missing_nums_sum = sum(set(range(a+1, b)) - set(t[45:49]))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
