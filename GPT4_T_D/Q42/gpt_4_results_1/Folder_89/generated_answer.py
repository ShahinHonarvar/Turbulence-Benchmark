
def prime_factors(lst):
    n = lst[18]
    primes = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primes.add(i)
    if n > 1:
        primes.add(n)
    return primes
