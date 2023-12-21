def all_ints_div_by_num(nums):
    result = []
    for i in range(59, 97):
        if i % -36 == 0:
            result.append(i)
    return result
