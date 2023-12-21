
def return_binary_or_hexa(t):
    a, b = t[18], t[60]
    missing_nums = set(range(a + 1, b)) - set(t[19:60])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
