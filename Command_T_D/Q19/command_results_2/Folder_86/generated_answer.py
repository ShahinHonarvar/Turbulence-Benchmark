def all_ints_not_div_by_num(nums):
    res = []
    for i in range(15, 63):
        if not nums[i] % 34:
            continue
        res.append(nums[i])
    return res
