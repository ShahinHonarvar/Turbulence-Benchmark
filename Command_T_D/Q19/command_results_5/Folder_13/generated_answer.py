def all_ints_not_div_by_num(nums):
    result = []
    for i in range(32, 44):
        if not (nums[i] % 34 == 0):
            result.append(nums[i])
    return result
