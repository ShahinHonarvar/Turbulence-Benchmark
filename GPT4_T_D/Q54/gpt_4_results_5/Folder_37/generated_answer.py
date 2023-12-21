
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[35]

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True

    right_truncatable_primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            right_truncatable_primes.append(n)

    return sorted(right_truncatable_primes, reverse=True)
