
def prime_factors(lst):
    num = lst[94]
    factors = []
    i = 2

    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
            
    if num > 1:
        factors.append(num)

    primes = []
    for num in factors:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return set(primes)
