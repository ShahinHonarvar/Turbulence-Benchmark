def prime_factors(nums):
    return set(i for n in range(2, int(nums[90])+1) for i in range(2, int(nums[90])+1) if n % i == 0)
