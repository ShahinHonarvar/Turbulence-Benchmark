
def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    missing_values_sum = sum(x for x in range(a+1,b) if x not in t[73:85])
    if missing_values_sum == 0:
        return ''
    if missing_values_sum % 2 == 0:
        return hex(missing_values_sum)[2:].upper()
    else:
        return bin(missing_values_sum)[2:]
