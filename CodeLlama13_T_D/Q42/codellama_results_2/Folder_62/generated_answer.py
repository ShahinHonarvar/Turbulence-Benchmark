
def prime_factors(numbers):
    return set([p for n in numbers if isprime(n) for p in prime_divisors(n)])
