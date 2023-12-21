
def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    not_in_tuple = set(range(a+1, b)) - set(t[10:29])
    result = sum(not_in_tuple)
    if result == 0:
        return ''
    elif result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]
