def prime_factors(nums):
    return set(i for i in range(2, int(nums[64]) + 1) if all(nums[i] == i or nums[i] == 1 for i in range(2, int(nums[64]) + 1)))
