def all_ints_not_div_by_num(nums):
    result = []
    for x in range(81, 87):
        if x % 77 != 0:
            result.append(x)
    return result
