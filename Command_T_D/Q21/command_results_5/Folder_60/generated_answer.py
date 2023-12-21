def all_ints_div_by_num(nums):
    result = []
    for i in range(31, 67):
        if i % -15 == 0:
            result.append(i)
    return result
