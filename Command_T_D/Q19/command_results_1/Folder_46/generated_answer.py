def all_ints_not_div_by_num(nums):
    result = []
    for i in range(18, 60):
        if nums[i] % 86 != 0:
            result.append(nums[i])
    return result
