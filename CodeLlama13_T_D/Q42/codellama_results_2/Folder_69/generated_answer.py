
def prime_factors(list):
    return set(prime_factorize(list[459]))

def prime_factorize(n):
    if n <= 1:
        return []
