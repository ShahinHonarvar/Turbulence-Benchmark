
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    factors_15 = find_factors(nums[15])
    factors_40 = find_factors(nums[40])
    
    common_factors = set(factors_15).intersection(factors_40)
    
    return max(common_factors)
