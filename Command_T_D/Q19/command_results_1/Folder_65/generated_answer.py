def all_ints_not_div_by_num(nums):
    result = []
    for i in range(15, 51):
        if not nums[i] % -34:
            continue
        result.append(nums[i])
    return result
