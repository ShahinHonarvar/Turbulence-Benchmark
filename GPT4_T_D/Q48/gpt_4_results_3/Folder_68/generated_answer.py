
def return_binary_or_hexa(t):
    a, b = t[0], t[9]
    sum_val = sum(set(range(a + 1, b)) - set(t[1:b]))
    if sum_val == 0:
        return ""
    elif sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]
