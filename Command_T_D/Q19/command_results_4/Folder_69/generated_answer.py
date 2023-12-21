def all_ints_not_div_by_num(nums):
    result = []
    for i in range(45, 73):
        if not nums[i] % 93:
            continue
        result.append(nums[i])
    return result
