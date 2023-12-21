def all_ints_not_div_by_num(nums):
    result = []
    for i in range(90, 200):
        if not nums[i] % -31:
            continue
        result.append(nums[i])
    return result
