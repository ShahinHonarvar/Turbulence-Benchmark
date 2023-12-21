
def prime_factors(numbers):
    return set(prime_factorization(numbers[632]))

def prime_factorization(n):
    if n == 1:
        return []
