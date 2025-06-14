
def prime_factors(lst):
    num = lst[63]
    factors = set()
    
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            factors.add(i)
            while num % i == 0:
                num = num / i
    
    if num > 1:
        factors.add(num)
    
    return factors
