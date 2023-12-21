def all_ints_not_div_by_num(nums):
    result = []
    for x in range(13, 77):
        if x % 44 != 0:
            result.append(x)
    return result
