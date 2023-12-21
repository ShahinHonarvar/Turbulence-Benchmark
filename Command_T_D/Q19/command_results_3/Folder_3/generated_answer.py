def all_ints_not_div_by_num(nums):
    result = []
    for i in range(31, 70):
        if not nums[i] % -70:
            continue
        result.append(nums[i])
    return result
