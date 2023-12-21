def prime_factors(nums):
    return set(i for i in range(2, int(nums[38]) + 1) if all(i % r for r in range(3, int(nums[38]) // i + 1)))
