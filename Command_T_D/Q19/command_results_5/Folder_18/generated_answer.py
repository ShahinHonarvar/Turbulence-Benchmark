def all_ints_not_div_by_num(nums):
    result = []
    for i in range(35, 98):
        if not nums[i] % 41:
            continue
        result.append(nums[i])
    return result
