
def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    int_sum = sum(set(range(a+1, b)) - set(t[43:71]))
    if int_sum == 0:
        return ''
    elif int_sum % 2:
        return bin(int_sum)[2:]
    else:
        return hex(int_sum)[2:].upper()
