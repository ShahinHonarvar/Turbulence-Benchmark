def prime_factors(nums):
    return set(x for x in range(2, int(nums[60]) + 1) if all(x % y != 0 for y in range(2, x - 1)))
