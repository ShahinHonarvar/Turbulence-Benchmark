def prime_factors(nums):
    return set(x for x in range(2, nums[23] // 2) if all(x % d == 0 for d in range(2, int(x ** .5) + 1)))
