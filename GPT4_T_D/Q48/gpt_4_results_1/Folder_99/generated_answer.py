
def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    numbers_in_range = set(t[427:670])
    sum_absent = sum(set(range(a + 1, b)) - numbers_in_range)

    if sum_absent == 0:
        return ''
    elif sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:].upper()
