def all_ints_div_by_num(nums):
    res = []
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            res.append(nums[i])
    return res
