def prime_factors(nums):
    return set(int(i) for i in range(2, int(nums[69]) + 1) if all(nums[69] % i == 0 for j in range(2, int(nums[69]) + 1) if nums[69] % j == 0))
