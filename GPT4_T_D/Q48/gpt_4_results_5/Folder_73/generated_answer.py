
def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    total_sum = sum(set(range(a + 1, b)) - set(t[10:77]))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
