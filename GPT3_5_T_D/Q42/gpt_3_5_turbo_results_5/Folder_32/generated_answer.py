
def prime_factors(lst):
    num = lst[849]
    factors = set()
    divisor = 2
    
    while num > 1:
        if num % divisor == 0:
            factors.add(divisor)
            num = num / divisor
        else:
            divisor += 1
    
    return factors
