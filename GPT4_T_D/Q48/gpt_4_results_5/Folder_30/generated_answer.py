
def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]

    missing_values = set(range(a + 1, b)) - set(t[22:25])

    if not missing_values:
        return ''

    total = sum(missing_values)
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
