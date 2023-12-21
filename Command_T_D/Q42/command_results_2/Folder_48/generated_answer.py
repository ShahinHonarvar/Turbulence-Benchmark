def prime_factors(nums):
    return set(int(n) for n in range(2,int(nums[0])+1) if all(nums[0]%n!=0 for n in range(2,int(nums[0])+1)))
