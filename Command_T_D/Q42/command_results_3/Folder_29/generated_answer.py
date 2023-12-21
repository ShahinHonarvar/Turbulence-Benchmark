def prime_factors(nums):
    return set(i for i in range(2, nums[19] + 1) if all(nums[19] % i == 0 for j in range(2, i // 2 + 1)))
