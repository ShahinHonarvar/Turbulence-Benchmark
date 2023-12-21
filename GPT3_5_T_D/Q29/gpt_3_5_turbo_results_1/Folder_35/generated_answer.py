
def gcf_two_nums(nums):
    def find_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    factors_380 = find_factors(nums[380])
    factors_327 = find_factors(nums[327])
    common_factors = list(set(factors_380) & set(factors_327))
    return max(common_factors)
