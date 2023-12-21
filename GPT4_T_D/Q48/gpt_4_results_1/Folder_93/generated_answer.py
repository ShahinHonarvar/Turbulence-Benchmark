
def return_binary_or_hexa(tup):
    a = tup[57]
    b = tup[85]
    missing_numbers = set(range(a + 1, b)) - set(tup[57:86])
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
