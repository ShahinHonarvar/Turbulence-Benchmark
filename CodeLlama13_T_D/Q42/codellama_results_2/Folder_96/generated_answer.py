
def prime_factors(mylist):
    return set(prime_factorization(mylist[47]))

def prime_factorization(n):
    if n == 1:
        return []
