def prime_factors(nums):
    return set(int(i) for i in range(2,int(nums[85])+1) if all(nums[85]%i!=0 for i in range(2,int(nums[85])+1)))
