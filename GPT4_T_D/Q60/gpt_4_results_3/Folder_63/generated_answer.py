
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_truncatable(p):
        p = str(p)
        if '0' in p:
            return False
        return all(isprime(int(p[i:])) and isprime(int(p[:len(p)-i])) for i in range(len(p)))

    x = tup[88]
    truncatable_primes = [i for i in range(11, x + 1) if is_truncatable(i) and isprime(i)]

    return sorted(truncatable_primes)
