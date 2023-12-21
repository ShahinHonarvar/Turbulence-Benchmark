
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = sorted(numbers)[792]
    all_primes = [2, 3, 5, 7]
    for start in all_primes[:]:
        for j in range(1, 10):
            n = int(str(start) + str(j))
            if n < x and isprime(n):
                all_primes.append(n)
    return sorted(all_primes)

def is_left_truncatable(p):
    if '0' in str(p):
        return False
    while p > 0:
        if not isprime(p):
            return False
        p = int(str(p)[1:]) if str(p)[1:] else 0
    return True
