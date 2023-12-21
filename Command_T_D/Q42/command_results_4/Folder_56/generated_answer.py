def prime_factors(nums):
    return set(i for i in range(2, nums[60]) if all(nums[i] % j == 0 for j in range(2, int(nums[i] ** .5) + 1)))
