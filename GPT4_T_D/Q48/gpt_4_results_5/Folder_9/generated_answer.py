
def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[70]
    b = nums_tuple[200]
    missing_nums = set(range(a + 1, b)) - set(nums_tuple[70:201])
    sum_of_missing = sum(missing_nums)
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing%2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]
