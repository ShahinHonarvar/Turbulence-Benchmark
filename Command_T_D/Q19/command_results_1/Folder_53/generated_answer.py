def all_ints_not_div_by_num(nums):
    result = []
    for i in range(199, 201):
        if i % -200 != 0:
            result.append(i)
    return result
