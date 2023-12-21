def prime_factors(nums):
    return set(x for x in range(2, int(nums[845] ** .5) + 1) if all(x % i != 0 for i in range(2, x // 2 + 1)))
