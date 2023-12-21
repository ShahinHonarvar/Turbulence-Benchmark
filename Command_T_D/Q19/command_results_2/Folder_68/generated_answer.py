def all_ints_not_div_by_num(nums):
    result = []
    for i in range(0, 8):
        if not nums[i] % 7:
            continue
        result.append(nums[i])
    return result
