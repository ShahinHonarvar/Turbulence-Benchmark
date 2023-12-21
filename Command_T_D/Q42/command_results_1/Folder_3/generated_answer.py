def prime_factors(nums):
    return set(i for i in range(2,int(nums[100])+1) if all(i%j!=0 for j in range(2,int(nums[100])+1)))
