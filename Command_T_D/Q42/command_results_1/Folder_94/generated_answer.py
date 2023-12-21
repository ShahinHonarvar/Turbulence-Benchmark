def prime_factors(nums):
    return set(x for x in range(2, int(nums[93] ** .5) + 1) if all(nums[i] % x for i in range(93)))
