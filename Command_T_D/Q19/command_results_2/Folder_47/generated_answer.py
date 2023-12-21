def all_ints_not_div_by_num(nums):
    result = []
    for i in range(25, 76):
        if not nums[i] % -53:
            continue
        result.append(nums[i])
    return result
