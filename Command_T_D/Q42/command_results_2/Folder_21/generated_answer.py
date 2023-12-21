def prime_factors(nums):
    return set(x for x in range(2, nums[0]) if all(x % r for r in range(3, int(x ** .5) + 1, 2)))
