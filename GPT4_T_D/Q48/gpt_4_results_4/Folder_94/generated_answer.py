
def return_binary_or_hexa(num_tuple):
    a = num_tuple[42]
    b = num_tuple[87]
    missing_nums = set(range(a+1, b)) - set(num_tuple[42:87+1])
    sum_nums = sum(missing_nums)
    if sum_nums % 2 == 0:
        return format(sum_nums, 'x')
    else:
        return format(sum_nums, 'b')
