
def find_primes_between_indices(lst):
    from sympy import isprime

    primes = [i for i in lst[72:73] if isprime(i)]
    primes.sort()
    
    return primes
