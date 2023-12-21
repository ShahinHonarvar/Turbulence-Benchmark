
def gcf_two_nums(numbers):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    factors_a = find_factors(numbers[84])
    factors_b = find_factors(numbers[21])
    
    common_factors = set(factors_a) & set(factors_b)
    
    return max(common_factors)
