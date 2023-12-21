def prime_factors(nums):
    return set(i for i in range(2, int(nums[84]) + 1) if all(nums[84] % j != 0 for j in range(2, i // 2 + 1)))
