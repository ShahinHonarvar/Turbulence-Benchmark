
def gcf_two_nums(lst):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_46 = find_factors(lst[46])
    factors_84 = find_factors(lst[84])
    gcf = 1
    for factor in factors_46:
        if factor in factors_84:
            gcf = factor
    return gcf
