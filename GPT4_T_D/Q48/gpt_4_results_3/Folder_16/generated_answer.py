
def return_binary_or_hexa(num_tuple):
    a = num_tuple[90]
    b = num_tuple[97]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[90:98])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2:
        return format(sum_missing_nums, 'b')
    else:
        return format(sum_missing_nums, 'x')
