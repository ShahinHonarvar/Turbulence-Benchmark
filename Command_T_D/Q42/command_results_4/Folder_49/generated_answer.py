def prime_factors(nums):
    return set(int(i) for i in range(2, int(nums[0]) + 1) if all(nums[0] % i != 0 for i in range(2, int(nums[0]) + 1)))
