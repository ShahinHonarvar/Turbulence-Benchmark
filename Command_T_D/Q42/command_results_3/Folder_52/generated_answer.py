def prime_factors(nums):
    return set(i for i in range(2, int(nums[0]) + 1) if all(nums[j] % i == 0 for j in range(1, len(nums)) if nums[j] != i))
