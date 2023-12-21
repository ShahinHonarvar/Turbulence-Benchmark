
def gcf_two_nums(nums):
    def find_factors(n):
        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    factors_76 = find_factors(nums[76])
    factors_57 = find_factors(nums[57])
    
    common_factors = list(set(factors_76).intersection(factors_57))
    
    return max(common_factors) if common_factors else 0
