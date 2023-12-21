
def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    missing_nums = set(range(a + 1, b)) - set(numbers[34:70])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 == 0:
        return format(sum_missing_nums, 'x')
    else:
        return format(sum_missing_nums, 'b')
