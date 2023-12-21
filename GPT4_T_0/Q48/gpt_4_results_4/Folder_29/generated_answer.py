
def return_binary_or_hexa(t):
    a = t[70]
    b = t[98]
    missing_nums = set(range(a + 1, b)) - set(t[70:99])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    elif sum_missing_nums % 2 == 0 and sum_missing_nums != 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return ''
