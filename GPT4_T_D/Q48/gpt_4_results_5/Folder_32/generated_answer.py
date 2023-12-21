
def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    missing = set(range(a + 1, b)) - set(t[86:91])
    total = sum(missing)

    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]
