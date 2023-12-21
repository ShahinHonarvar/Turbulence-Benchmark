def all_ints_not_div_by_num(nums):
    result = []
    for i in range(48, 62):
        if not (nums[i] % 28 == 0):
            result.append(nums[i])
    return result
