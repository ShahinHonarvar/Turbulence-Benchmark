
def gcf_two_nums(nums):

    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_20 = find_factors(nums[20])
    factors_83 = find_factors(nums[83])
    common_factors = set(factors_20).intersection(factors_83)
    gcf = max(common_factors)
    
    return gcf
