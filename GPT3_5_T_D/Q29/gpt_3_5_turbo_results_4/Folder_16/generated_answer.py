
def gcf_two_nums(nums):
    def find_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    factors_860 = find_factors(nums[860])
    factors_307 = find_factors(nums[307])
    
    common_factors = set(factors_860).intersection(factors_307)
    
    return max(common_factors)
