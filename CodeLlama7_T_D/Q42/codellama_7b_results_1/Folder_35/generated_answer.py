
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return set([i]) | prime_factors(n // i)
