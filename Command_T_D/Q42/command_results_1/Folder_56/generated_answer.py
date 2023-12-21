def prime_factors(nums):
    return set(i for i in range(2, nums[60]) if all(nums[j] % i != 0 for j in range(1, nums[60] // i + 1)))
