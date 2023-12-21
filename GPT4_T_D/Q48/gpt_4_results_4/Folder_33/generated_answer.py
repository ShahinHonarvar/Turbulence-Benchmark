
def return_binary_or_hexa(t):
    a, b = t[13], t[35]
    missing_nums = set(range(a + 1, b)) - set(t[13:36])
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
    return ""
