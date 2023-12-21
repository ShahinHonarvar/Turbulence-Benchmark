
def gcf_two_nums(nums):
    def find_factors(n):
        factors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                factors.add(i)
        return factors

    factors_29 = find_factors(nums[29])
    factors_53 = find_factors(nums[53])
    common_factors = factors_29.intersection(factors_53)
    return max(common_factors)
