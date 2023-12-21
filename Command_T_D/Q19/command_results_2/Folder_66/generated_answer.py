def all_ints_not_div_by_num(nums):
    result = []
    for i in range(84, 86):
        if nums[i] % 99 != 0:
            result.append(nums[i])
    return result
