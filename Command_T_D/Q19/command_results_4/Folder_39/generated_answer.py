def all_ints_not_div_by_num(nums):
    res = []
    for i in range(22, 97):
        if not nums[i] % -46:
            break
        res.append(nums[i])
    return res
