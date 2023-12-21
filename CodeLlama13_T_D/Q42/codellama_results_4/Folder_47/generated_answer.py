
def prime_factors(numbers):
    return set(prime_factorize(numbers[34]))

def prime_factorize(n):
    if n == 1:
        return []
