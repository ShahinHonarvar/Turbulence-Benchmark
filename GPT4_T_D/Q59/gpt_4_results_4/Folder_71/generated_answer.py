
from sympy import primerange

def all_left_truncatable_prime(t):
    limit = t[22]
    primes = list(primerange(1, limit))
    left_truncable_primes = []

    for prime in primes:
        if '0' in str(prime):
            continue
        else:
            str_prime=str(prime)
            is_truncable = True
            for i in range(len(str_prime)):
                if int(str_prime[i:]) not in primes:
                    is_truncable = False
                    break
            if is_truncable:
                left_truncable_primes.append(prime)
            
    return sorted(left_truncable_primes, reverse=True)
