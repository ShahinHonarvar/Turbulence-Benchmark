
def find_primes_between_indices(lst):
    from sympy import isprime
    
    primes = [i for i in lst[167:786] if isprime(i)]
    primes.sort(reverse=True)
    
    return primes
