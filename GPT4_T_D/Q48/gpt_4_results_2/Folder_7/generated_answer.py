
def return_binary_or_hexa(t):
    a = t[10]
    b = t[97]
    absent = set(range(a + 1, b)) - set(t[10:97])
    sum_absent = sum(absent)

    if sum_absent == 0:
        return ''
    elif sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:].upper()
