
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[11]
    left_truncatable_primes = []
    for num in range(11, x):
        if num == 0 or '0' in str(num):
            continue

        truncatable_check = all(isprime(int(str(num)[i:])) for i in range(len(str(num))))
        if isprime(num) and truncatable_check:
            left_truncatable_primes.append(num)
            
    return sorted(left_truncatable_primes)
