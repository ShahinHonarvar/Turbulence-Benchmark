
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[36]
    primes = []

    def is_left_truncatable(n):
        if n < 10:
            return isprime(n)
        else:
            if isprime(n) and '0' not in str(n):
                return is_left_truncatable(int(str(n)[1:]))
            else:
                return False

    for num in range(2, x):
        if is_left_truncatable(num):
            primes.append(num)

    return sorted(primes)
