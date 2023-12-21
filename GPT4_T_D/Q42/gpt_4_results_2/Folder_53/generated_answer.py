
def prime_factors(lst):
    num = lst[73]
    factors = set()
    factor = 2
    
    while factor * factor <= num:
        if num % factor:
            factor += 1
        else:
            num //= factor
            factors.add(factor)
    if num > 1:
        factors.add(num)
        
    return factors
