
def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    missing_nums = set(range(a+1, b)) - set(t[19:60])
    total = sum(missing_nums)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
