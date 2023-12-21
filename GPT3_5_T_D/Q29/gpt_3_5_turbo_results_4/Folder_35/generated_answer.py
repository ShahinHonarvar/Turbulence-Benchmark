
def gcf_two_nums(nums):
    def find_factors(n):
        factors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        return factors

    factors_380 = find_factors(nums[380])
    factors_327 = find_factors(nums[327])
    common_factors = factors_380 & factors_327
    
    return max(common_factors)
