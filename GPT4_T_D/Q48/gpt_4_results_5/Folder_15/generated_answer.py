
def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[4]

    missing_nums = [x for x in range(a + 1, b) if x not in tup[0:5]]
    
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 != 0:
        return format(sum_missing_nums, 'b')
    else:
        return format(sum_missing_nums, 'X')
