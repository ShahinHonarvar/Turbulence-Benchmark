def prime_factors(nums):
    return set(x for x in range(2, int(nums[64] ** .5) + 1) if all(x % r == 0 for r in range(2, x // 2)))
