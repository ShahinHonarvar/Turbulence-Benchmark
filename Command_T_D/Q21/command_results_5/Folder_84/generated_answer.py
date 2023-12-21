def all_ints_div_by_num(nums):
    result = []
    for i in range(52, 53):
        if (i * 93) in nums:
            result.append(i * 93)
    return result
