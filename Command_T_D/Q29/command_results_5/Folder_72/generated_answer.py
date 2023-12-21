def gcf_two_nums(nums):
    return next(n for n in range(min(nums), int(nums[18] / 2) + 1) if nums[18] % n == nums[37] % n)
