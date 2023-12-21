def prime_factors(nums):
    return set(i for i in range(2, int(nums[87]) + 1) if all(nums[87] % i for j in range(2, i)))
