
def prime_factors(lst):
    num = lst[100]
    factors = set()
    
    for i in range(2, int(num**0.5)+1):
        while num % i == 0:
            factors.add(i)
            num //= i
    
    if num > 1:
        factors.add(num)
    
    return factors
