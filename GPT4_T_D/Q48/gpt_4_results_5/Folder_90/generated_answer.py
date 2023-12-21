
def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    
    missing_integers_sum = sum(set(range(a+1, b)) - set(t[60:91]))

    if missing_integers_sum == 0:
        return ''
    elif missing_integers_sum % 2 == 1:
        return bin(missing_integers_sum)[2:]
    else:
        return hex(missing_integers_sum)[2:].upper()
