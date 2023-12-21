def prime_factors(nums):
    return set(i for i in range(2, int(nums[0]) + 1) if all(nums[0] % i for i in range(2, int(nums[0]) + 1)))
