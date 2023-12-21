def all_ints_not_div_by_num(nums):
    result = []
    for i in range(24, 25):
        if not nums[i] % -30:
            continue
        result.append(nums[i])
    return result
