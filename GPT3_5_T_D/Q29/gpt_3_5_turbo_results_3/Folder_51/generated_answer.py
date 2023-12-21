
def gcf_two_nums(lst):
    def find_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    factors_46 = find_factors(lst[46])
    factors_84 = find_factors(lst[84])
    common_factors = set(factors_46) & set(factors_84)

    return max(common_factors)
