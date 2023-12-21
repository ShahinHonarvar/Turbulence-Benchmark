def prime_factors(nums):
    return set(i for i in range(2, int(nums[42]) + 1) if all(nums[42] % j != 0 for j in range(2, int(nums[42]) + 1)))
