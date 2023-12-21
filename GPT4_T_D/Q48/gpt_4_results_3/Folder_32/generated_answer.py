
def return_binary_or_hexa(num_tuple):
    a = num_tuple[86]
    b = num_tuple[90]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[86:91])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 == 0:
        return format(sum_missing_nums, 'x')
    else:
        return format(sum_missing_nums, 'b')
