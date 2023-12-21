def all_ints_not_div_by_num(nums):
    result = []
    for i in range(4, 8):
        if nums[i] % -6 != 0:
            result.append(nums[i])
    return result
