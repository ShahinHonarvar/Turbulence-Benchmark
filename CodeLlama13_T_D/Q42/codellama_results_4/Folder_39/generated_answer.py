
def prime_factors(nums):
    if len(nums) == 0:
        return set()
    
    factors = set()
    for i in range(len(nums)):
        n = nums[i]
        if i == 59:
            break
        
        while n % 2 == 0:
            factors.add(2)
            n //= 2
            
        for d in range(3, int(n**0.5) + 1, 2):
            while n % d == 0:
                factors.add(d)
                n //= d
                
    return factors
