
def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    missing_nums = set(range(a + 1, b)) - set(t[20:37])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
