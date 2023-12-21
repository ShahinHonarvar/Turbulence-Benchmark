
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num+1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_634 = find_factors(nums[634])
    factors_585 = find_factors(nums[585])

    common_factors = list(set(factors_634) & set(factors_585))
    greatest_common_factor = max(common_factors)
    
    return greatest_common_factor
