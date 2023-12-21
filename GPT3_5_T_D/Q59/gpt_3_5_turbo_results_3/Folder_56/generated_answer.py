
from sympy import isprime

def is_left_truncatable_prime(n):
    n = str(n)
    for i in range(len(n)):
        if not isprime(int(n[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[30]
    primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)
