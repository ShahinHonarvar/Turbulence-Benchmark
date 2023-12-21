def prime_factors(nums):
    return set(i for i in range(2, nums[38]) if all(nums[38] % j != 0 for j in range(2, i + 1)))
