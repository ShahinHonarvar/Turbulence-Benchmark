
def gcf_two_nums(lst):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    factors_28 = find_factors(lst[28])
    factors_49 = find_factors(lst[49])
    
    common_factors = list(set(factors_28) & set(factors_49))
    
    gcf = max(common_factors)
    return gcf
