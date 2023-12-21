def prime_factors(nums):
    return set(range(2, int(nums[0]) + 1)) & {i for i in range(2, int(nums[0]) + 1) if all(nums[0] % j != 0 for j in range(2, i - 1))]
