def all_ints_not_div_by_num(nums):
    result = []
    for i in range(24, 25):
        if nums[i] % -30 != 0:
            result.append(nums[i])
    return result
