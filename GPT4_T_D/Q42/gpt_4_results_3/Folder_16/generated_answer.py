
def prime_factors(lst):
    num = lst[162]
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
        
    primes = set()
    for num in factors:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primes.add(num)
    return primes
