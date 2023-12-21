def prime_factors(nums):
    return set(i for i in range(2, int(nums[993]) + 1) if all(nums[k] % i != 0 for k in range(993, -1, -1)))
