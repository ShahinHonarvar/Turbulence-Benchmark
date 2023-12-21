
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    factors_7 = find_factors(nums[7])
    factors_9 = find_factors(nums[9])

    common_factors = []
    for factor in factors_7:
        if factor in factors_9:
            common_factors.append(factor)

    return max(common_factors)
