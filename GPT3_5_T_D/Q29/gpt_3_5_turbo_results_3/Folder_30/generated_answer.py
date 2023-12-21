
def gcf_two_nums(lst):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    def find_gcf(a, b):
        factors_a = find_factors(a)
        factors_b = find_factors(b)
        common_factors = list(set(factors_a) & set(factors_b))
        return max(common_factors)
    
    return find_gcf(lst[85], lst[33])
