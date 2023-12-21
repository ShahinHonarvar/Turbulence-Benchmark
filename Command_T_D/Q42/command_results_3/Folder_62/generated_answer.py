def prime_factors(nums):
    return set(x for x in range(2, int(nums[926] ** .5) + 1) if all(x % d == 0 for d in range(3, int(x ** .5) + 1, 2)))
