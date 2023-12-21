def prime_factors(nums):
    return set(x for x in range(2, nums[0]//2) if all(x%y!=0 for y in range(2, int(x**(0.5))+1)))
