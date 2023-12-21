def all_ints_not_div_by_num(nums):
    result = []
    for i in range(24, 32):
        if not nums[i] % 35:
            continue
        else:
            result.append(nums[i])
    return result
