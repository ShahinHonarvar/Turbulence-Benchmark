def prime_factors(nums):
    return set(filter(lambda x: nums[0] % x == 0, range(2, nums[0] + 1)))
