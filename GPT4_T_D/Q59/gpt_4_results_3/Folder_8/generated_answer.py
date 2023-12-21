
from sympy import isprime

def left_truncatable(num):
    if '0' in str(num):
        return False
    num_str = str(num)
    for i in range(len(num_str)):
        if not isprime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[41]
    primes = []
    for num in range(2, x):
        if left_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)
