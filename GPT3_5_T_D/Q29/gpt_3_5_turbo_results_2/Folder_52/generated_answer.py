
def gcf_two_nums(numbers):
    def find_factors(n):
        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    num1 = numbers[90]
    num2 = numbers[41]
    
    factors1 = find_factors(num1)
    factors2 = find_factors(num2)
    
    common_factors = []
    for factor in factors1:
        if factor in factors2:
            common_factors.append(factor)
    
    return max(common_factors)
