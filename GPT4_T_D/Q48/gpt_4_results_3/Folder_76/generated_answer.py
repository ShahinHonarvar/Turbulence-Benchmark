
def return_binary_or_hexa(t):
    a, b = t[450], t[905]
    excluded_sum = sum(set(range(a + 1, b)) - set(t[450:906]))
    if excluded_sum % 2 == 1:
        return bin(excluded_sum)[2:]
    elif excluded_sum % 2 == 0 and excluded_sum != 0:
        return hex(excluded_sum)[2:]
    else:
        return ''
