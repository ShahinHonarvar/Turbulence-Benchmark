
def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    missing_nums = set(range(a + 1, b)) - set(tup[86:90])
    total = sum(missing_nums)
    if total == 0:
        return ""
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
