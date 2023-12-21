
def prime_factors(integers):
    num = integers[18]
    factors = set()
    i = 2
    
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    
    if num > 1:
        factors.add(num)
    
    return factors
