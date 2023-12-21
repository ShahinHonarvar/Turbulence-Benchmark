
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[73]

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    left_truncatable_primes = []
    for num in range(10, x):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)

    return sorted(left_truncatable_primes, reverse=True)
