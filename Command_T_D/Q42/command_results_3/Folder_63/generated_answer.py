def prime_factors(nums):
    return set(x for x in range(2, int(nums[57]) + 1) if all(x % i for i in range(2, x // 2)))
