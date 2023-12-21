
from sympy import isprime 

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[758]
    def is_left_truncatable_prime(p):
        if p < 10:
            return isprime(p)
        return isprime(p) and '0' not in str(p) and is_left_truncatable_prime(int(str(p)[1:]))
    primes = [i for i in range(1, x) if is_left_truncatable_prime(i)]
    return sorted(primes)
