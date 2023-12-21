def prime_factors(nums):
    return set(i for i in range(2, int(nums[96]) + 1) if all(nums[96] % j != 0 for j in range(2, int(nums[96]) + 1)))
