
def return_binary_or_hexa(t):
    a, b = t[86], t[99]
    missing_nums = set(range(a + 1, b)) - set(t[86:100])
    total = sum(missing_nums)
    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
