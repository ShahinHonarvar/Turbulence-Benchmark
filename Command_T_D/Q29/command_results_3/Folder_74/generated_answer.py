def gcf_two_nums(nums):
    return next((x for x in range(1, max(nums) + 1) if nums[36] % x == 0 and nums[85] % x == 0), -1)
