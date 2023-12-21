def prime_factors(nums):
    return set(x for x in range(2, int(nums[632]) + 1) if all(x % y for y in range(2, x // 2 + 1)))
