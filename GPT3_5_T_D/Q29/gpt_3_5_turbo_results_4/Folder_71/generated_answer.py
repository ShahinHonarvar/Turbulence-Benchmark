
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_78 = find_factors(nums[78])
    factors_93 = find_factors(nums[93])
    common_factors = set(factors_78) & set(factors_93)
    return max(common_factors)
