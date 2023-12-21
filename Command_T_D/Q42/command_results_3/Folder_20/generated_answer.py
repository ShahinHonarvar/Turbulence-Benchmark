def prime_factors(nums):
    return set(prime_factors(i) for i in range(2,int(nums[53])+1))
