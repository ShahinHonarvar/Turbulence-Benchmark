
def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    missing_numbers = set(range(a + 1, b)) - set(t[36:53])
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
