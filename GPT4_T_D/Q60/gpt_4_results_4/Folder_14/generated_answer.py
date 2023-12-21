
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[78]
    primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(1, len(str(num))):
            if not (isprime(int(str(num)[i:])) and isprime(int(str(num)[:-i]))):
                is_truncatable = False
                break
        if is_truncatable and isprime(num):
            primes.append(num)
    return sorted(primes, reverse=True)
