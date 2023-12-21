def prime_factors(nums):
    fac = {i for i in range(2, nums[43]) if all(nums[43] % i == 0 for j in range(2, i)))}
    return fac
