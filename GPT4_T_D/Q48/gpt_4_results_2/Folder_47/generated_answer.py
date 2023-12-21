
def return_binary_or_hexa(num_tuple):
    a = num_tuple[29]
    b = num_tuple[53]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[30:53])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return format(sum_missing_nums, 'b')
    elif sum_missing_nums % 2 == 0:
        return format(sum_missing_nums, 'X')
    else:
        return ''
