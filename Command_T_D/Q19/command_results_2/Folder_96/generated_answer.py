def all_ints_not_div_by_num(nums):
    result = []
    for i in range(50, 201):
        if i % -34 != 0:
            result.append(i)
    return result
