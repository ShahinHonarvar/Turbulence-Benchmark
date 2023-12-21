
def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    sum_res = sum(set(range(a + 1, b)) - set(t[60:91]))
    if sum_res % 2 == 1:
        return bin(sum_res)[2:]
    else:
        return hex(sum_res)[2:].upper()
