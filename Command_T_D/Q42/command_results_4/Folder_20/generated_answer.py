def prime_factors(nums):
    return set(i for i in range(2, int(nums[53]) + 1) if all(nums[k] % i for k in range(1, len(nums))))
