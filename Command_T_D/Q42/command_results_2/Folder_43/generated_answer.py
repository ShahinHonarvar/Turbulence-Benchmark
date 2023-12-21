def prime_factors(nums):
    return set(i for i in range(2, int(nums[29]) + 1) if all(nums[j] % i != 0 for j in range(29)))
