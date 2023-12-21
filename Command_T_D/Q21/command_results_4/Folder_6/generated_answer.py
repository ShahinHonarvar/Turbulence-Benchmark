def all_ints_div_by_num(nums):
    result = []
    for i in range(13, 63):
        if (i * 46) in nums:
            result.append(i * 46)
    return result
