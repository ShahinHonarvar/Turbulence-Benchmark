def prime_factors(nums):
    return set(int(i) for i in range(2, int(nums[72]) + 1) if all(nums[j] % i == 0 for j in range(1, nums[72] // i + 1)))
