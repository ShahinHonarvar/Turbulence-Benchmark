def all_ints_not_div_by_num(nums):
    res = []
    for i in range(59, 93):
        if not nums[i] % -26:
            continue
        res.append(nums[i])
    return res
