def all_ints_not_div_by_num(nums):
    res = []
    for i in range(62, 96):
        if not nums[i] % 26:
            continue
        res.append(nums[i])
    return res
