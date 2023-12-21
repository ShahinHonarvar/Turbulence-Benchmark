def all_ints_not_div_by_num(nums):
    result = []
    for i in range(81, 86):
        if not nums[i] % 77:
            continue
        result.append(nums[i])
    return result
