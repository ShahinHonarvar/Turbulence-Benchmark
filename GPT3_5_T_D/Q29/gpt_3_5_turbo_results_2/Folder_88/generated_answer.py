
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    factors_27 = find_factors(nums[27])
    factors_34 = find_factors(nums[34])
    
    common_factors = [factor for factor in factors_27 if factor in factors_34]
    
    return max(common_factors)
