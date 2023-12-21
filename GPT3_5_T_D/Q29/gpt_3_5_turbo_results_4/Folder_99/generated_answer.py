
def gcf_two_nums(lst):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_279 = find_factors(lst[279])
    factors_812 = find_factors(lst[812])
    common_factors = list(set(factors_279).intersection(factors_812))
    gcf = max(common_factors)
    return gcf
