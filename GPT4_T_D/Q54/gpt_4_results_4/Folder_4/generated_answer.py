
def all_right_truncatable_prime(tuple_of_positive_integers):
    import sympy
    x = tuple_of_positive_integers[96]
    all_primes = set(sympy.primerange(0, x))
    truncatable_primes = []
    
    for prime in all_primes:
        str_prime = str(prime)
        while str_prime:
            if int(str_prime) in all_primes:
                str_prime = str_prime[:-1]
            else:
                break
        if not str_prime:
            truncatable_primes.append(prime)
    
    return sorted(truncatable_primes, reverse=True)
