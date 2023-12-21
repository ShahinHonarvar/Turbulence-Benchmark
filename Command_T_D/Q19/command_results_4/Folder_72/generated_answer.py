def all_ints_not_div_by_num(nums):
    result = []
    for i in range(13, 71):
        if nums[i] % -78 != 0:
            result.append(nums[i])
    return result
