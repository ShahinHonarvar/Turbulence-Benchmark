
def prime_factors(n):
    # Find all factors of n
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.extend(prime_factors(n // i))
    return set(factors)
