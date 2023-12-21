def prime_factors(nums):
    return set(int(x) for x in range(2, int(nums[0]) + 1) if all(nums[0] % x == 0 for x in range(2, int(nums[0]) + 1)))
