
def return_binary_or_hexa(t):
    a, b = t[57], t[84]
    absent_nums = set(range(a + 1, b)) - set(t[57:85])
    sum_absent = sum(absent_nums)
    if sum_absent == 0:
        return ''
    elif sum_absent % 2:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:]
