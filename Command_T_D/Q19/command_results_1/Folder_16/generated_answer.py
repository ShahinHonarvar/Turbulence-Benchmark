def all_ints_not_div_by_num(nums):
    result = []
    for i in range(24, 33):
        if not nums[i] % 35:
            continue
        result.append(nums[i])
    return result
