
def gcf_two_nums(nums):
    def find_factors(num):
        factors = [i for i in range(1, num + 1) if num % i == 0]
        return factors
    
    factors_64 = find_factors(nums[64])
    factors_28 = find_factors(nums[28])
    
    common_factors = set(factors_64) & set(factors_28)
    
    if len(common_factors) == 0:
        return 1
    
    return max(common_factors)
