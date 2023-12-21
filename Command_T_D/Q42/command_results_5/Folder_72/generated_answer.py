def prime_factors(nums):
    return set(x for x in range(2, nums[16]) if all(nums[i] % x for i in range(1, nums[16] + 1)))
