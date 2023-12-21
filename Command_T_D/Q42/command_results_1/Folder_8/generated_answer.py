def prime_factors(nums):
    return set(i for i in range(2, int(nums[49]) + 1) if all(i not in nums for j in range(2, int(i**(0.5)) + 1)))
