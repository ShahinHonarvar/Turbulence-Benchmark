def all_ints_not_div_by_num(nums):
    result = []
    for i in range(22, 97):
        if i % -46 == 0:
            continue
        result.append(i)
    return result
