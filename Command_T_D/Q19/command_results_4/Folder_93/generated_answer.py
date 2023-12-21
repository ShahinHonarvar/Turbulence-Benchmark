def all_ints_not_div_by_num(nums):
    result = []
    for i in range(33, 78):
        if i % -17 != 0:
            result.append(i)
    return result
