def all_pos_ints_inclusive(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(nums[i])
    return res
