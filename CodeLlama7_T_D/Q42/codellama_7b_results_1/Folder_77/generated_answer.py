
def prime_factors(n):
    # find all prime factors of n
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    return set(factors)
