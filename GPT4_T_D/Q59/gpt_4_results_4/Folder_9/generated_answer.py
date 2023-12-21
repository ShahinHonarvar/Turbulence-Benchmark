
from sympy import isprime

def is_left_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        if not isprime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[29]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
