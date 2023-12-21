def all_pos_ints_exclusive(nums):
    res = []
    for i in range(20, 51):
        if i in nums:
            res += nums[:i] + nums[i+1:]
            break
    return res
