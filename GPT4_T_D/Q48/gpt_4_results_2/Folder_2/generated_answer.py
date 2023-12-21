
def return_binary_or_hexa(num_tuple):
    a = num_tuple[72]
    b = num_tuple[93]
    missing_nums = set(range(a+1, b)) - set(num_tuple[72:93])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
