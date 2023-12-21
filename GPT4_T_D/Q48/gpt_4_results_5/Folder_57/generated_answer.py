
def return_binary_or_hexa(t):
    a = t[25]
    b = t[80]
    excluded_sum = sum(set(range(a + 1, b)) - set(t[25:81]))
    if excluded_sum % 2 != 0:
        return bin(excluded_sum)[2:]
    else:
        return hex(excluded_sum)[2:].upper()
