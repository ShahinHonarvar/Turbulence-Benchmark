
from sympy import isprime

def all_left_truncatable_prime(tup):
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    limit = tup[41]
    truncatable_primes = [i for i in range(2, limit) if is_left_truncatable_prime(i)]
    return sorted(truncatable_primes)
