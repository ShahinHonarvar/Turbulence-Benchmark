
def prime_factors(nums):
    if len(nums) == 0:
        return set()
    
    factors = set()
    for i in range(126, len(nums)):
        num = nums[i]
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                factors.add(j)
        
    return factors
