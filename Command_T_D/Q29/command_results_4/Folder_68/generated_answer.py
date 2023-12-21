def gcf_two_nums(nums):
    return max(x for x in range(min(nums),0,-1) if nums[8] % x == nums[9] % x)
