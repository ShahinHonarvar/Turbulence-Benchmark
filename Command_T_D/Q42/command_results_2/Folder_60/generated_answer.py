def prime_factors(nums):
    return set(i for i in range(2, int(nums[88]) + 1) if all(i % j != 0 for j in range(2, i // 2 + 1)))
