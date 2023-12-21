def all_ints_not_div_by_num(nums):
    result = []
    for i in range(40, 200):
        if not (i % 71 == 0):
            result.append(i)
    return result
