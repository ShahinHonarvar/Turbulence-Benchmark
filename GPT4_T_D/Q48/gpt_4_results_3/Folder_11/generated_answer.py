
def return_binary_or_hexa(t):
    a = t[48]
    b = t[76]
    missing = set(range(a + 1, b)) - set(t[48:77])
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()
