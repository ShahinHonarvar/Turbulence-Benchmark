def prime_factors(nums):
    return set(i for i in range(2, int(nums[56])+1) if all(nums[56] % j for j in range(2, i-1)))
