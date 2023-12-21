def gcf_two_nums(nums):
    return next(x for x in range(2, min(nums) // 2 + 1) if all(n % x == 0 for n in nums))
