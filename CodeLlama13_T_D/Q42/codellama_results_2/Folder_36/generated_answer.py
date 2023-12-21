
def prime_factors(my_list):
    return set(prime_factorization(my_list[990]))

def prime_factorization(n):
    if n == 1:
        return []
