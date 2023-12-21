def prime_factors(nums):
    return set(x for x in range(2, nums[222] // 2 + 1) if all(nums[222] % x == 0 for x in range(3, int(nums[222] ** .5) + 1)))
