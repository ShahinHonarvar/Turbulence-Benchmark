
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[8]
    truncatable_primes = []
    for i in range(2, x):
        if isprime(i) and '0' not in str(i):
            is_truncatable = True
            for j in range(1, len(str(i))):
                if not isprime(int(str(i)[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
