def prime_factors(nums):
    return set(int(i) for i in range(2,int(nums[23])+1) if all(x%i!=0 for x in nums))
