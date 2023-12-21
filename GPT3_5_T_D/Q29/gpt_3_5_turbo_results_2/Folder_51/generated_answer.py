
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    factors_46 = find_factors(nums[46])
    factors_84 = find_factors(nums[84])
    
    common_factors = list(set(factors_46) & set(factors_84))
    
    return max(common_factors)
