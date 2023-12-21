def prime_factors(nums):
    return set(int(i) for i in range(1, int(nums[69]) + 1) if all(nums[i] % j != 0 for j in range(3, int(nums[i]) + 1)))
