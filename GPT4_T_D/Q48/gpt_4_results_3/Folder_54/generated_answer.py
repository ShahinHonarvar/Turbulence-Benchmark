
def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    missing_nums = set(range(a + 1, b)) - set(t[36:64])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ''
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
