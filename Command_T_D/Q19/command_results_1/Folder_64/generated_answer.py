def all_ints_not_div_by_num(nums):
    res = []
    for i in range(2, len(nums) - 1):
        if not nums[i] % 2:
            continue
        res.append(nums[i])
    return res
