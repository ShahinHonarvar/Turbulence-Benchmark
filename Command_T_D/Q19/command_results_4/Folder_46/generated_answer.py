def all_ints_not_div_by_num(nums):
    result = []
    for i in range(18, 60):
        if not nums[i] % 86:
            continue
        result.append(nums[i])
    return result
