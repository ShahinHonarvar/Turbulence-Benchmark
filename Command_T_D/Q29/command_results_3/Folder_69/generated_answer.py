def gcf_two_nums(nums):
    return next(num for num in range(min(nums), max(nums) + 1) if num > 1 and all(num == gcd(num, n) for n in nums))
