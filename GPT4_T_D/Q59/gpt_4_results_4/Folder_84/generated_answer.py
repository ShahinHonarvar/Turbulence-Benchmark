
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[630]

    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    primes = [i for i in range(2, x) if isprime(i) and is_left_truncatable(i)]
    primes.sort(reverse=True)
    return primes
