def all_pos_ints_inclusive(nums):
    res = []
    for i in range(20, 200):
        if i in nums:
            res += nums[i]
    return res
