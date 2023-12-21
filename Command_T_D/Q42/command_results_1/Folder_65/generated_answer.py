def prime_factors(nums):
    return set(x for x in range(2, nums[35] + 1) if all(x % i != 0 for i in range(2, x // 2)))
