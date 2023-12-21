
def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    missing_nums = set(range(a + 1, b)) - set(t[30:201])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return format(sum_missing_nums, 'x')
    else:
        return format(sum_missing_nums, 'b')
