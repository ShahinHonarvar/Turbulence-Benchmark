def prime_factors(nums):
    return set(i for i in range(1, int(nums[0]) + 1) if all(nums[0] % j != 0 for j in range(2, int(nums[0]) + 1)))
