
from sympy import isprime

def all_left_truncatable_prime(ints):
    x = ints[429]
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if str_n.count('0') > 0:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    for i in range(10, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
            
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
