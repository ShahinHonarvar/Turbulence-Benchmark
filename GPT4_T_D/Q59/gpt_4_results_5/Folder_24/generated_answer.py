
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[65]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' not in str_num:
            for i in range(len(str_num)):
                if not isprime(int(str_num[i:])):
                    break
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
