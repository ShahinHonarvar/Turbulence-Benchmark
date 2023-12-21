
def gcf_two_nums(numbers):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    factors_129 = find_factors(numbers[129])
    factors_582 = find_factors(numbers[582])
    
    common_factors = set(factors_129) & set(factors_582)
    
    return max(common_factors)
