
def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    missing_values = set(range(a + 1, b)) - set(t[275:872])
    total = sum(missing_values)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
