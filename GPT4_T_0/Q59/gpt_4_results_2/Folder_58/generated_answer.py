
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[975]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_left_truncatable = True
        while len(num_str) > 0:
            if not isprime(int(num_str)):
                is_left_truncatable = False
                break
            num_str = num_str[1:]
        if is_left_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)
