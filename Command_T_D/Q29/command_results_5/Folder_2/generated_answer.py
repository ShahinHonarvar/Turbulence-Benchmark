def gcf_two_nums(nums):
    return next(n for n in range(min(nums), max(nums) + 1) if all(n % a == 0 for a in nums))
