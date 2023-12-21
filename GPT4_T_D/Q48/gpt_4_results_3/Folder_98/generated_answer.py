
def return_binary_or_hexa(t):
    a, b = t[6], t[7]
    total_sum = sum(set(range(a+1, b)) - set(t[6:7+1]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
