
def prime_factors(lst):
    return set(prime_factorization(lst[247]))

def prime_factorization(n):
    if n == 1:
        return []
