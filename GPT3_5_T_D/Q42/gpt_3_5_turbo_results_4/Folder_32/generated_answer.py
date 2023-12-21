
def prime_factors(lst):
    num = lst[849]
    factors = set()
    
    if num < 2:
        return factors
    
    while num % 2 == 0:
        factors.add(2)
        num = num // 2
    
    divisor = 3
    
    while divisor * divisor <= num:
        if num % divisor == 0:
            factors.add(divisor)
            num = num // divisor
        else:
            divisor += 2
    
    if num > 1:
        factors.add(num)
    
    return factors
