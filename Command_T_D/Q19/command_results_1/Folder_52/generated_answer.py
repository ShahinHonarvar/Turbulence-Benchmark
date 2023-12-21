def all_ints_not_div_by_num(nums):
    result = []
    for i in range(50, 92):
        if not nums[i] % 16:
            continue
        result.append(nums[i])
    return result
