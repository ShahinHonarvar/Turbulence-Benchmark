def all_ints_div_by_num(nums):
    result = []
    for i in range(36, 40):
        if nums[i] % 28 == 0:
            result.append(nums[i])
    return result
