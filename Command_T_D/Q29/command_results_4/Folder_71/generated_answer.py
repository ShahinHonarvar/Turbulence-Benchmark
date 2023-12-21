def gcf_two_nums(nums):
    return next(x for x in range(1, max(nums) + 1) if all(x % y == 0 for y in nums))
