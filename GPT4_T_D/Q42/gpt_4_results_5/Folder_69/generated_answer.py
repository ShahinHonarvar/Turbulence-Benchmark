
def prime_factors(lst):
    num = lst[459]
    primes = set()
    factor = 2
    
    while factor * factor <= num:
        if num % factor:
            factor += 1
        else:
            num //= factor
            primes.add(factor)
      
    if num != 1:
        primes.add(num)
    
    return primes
