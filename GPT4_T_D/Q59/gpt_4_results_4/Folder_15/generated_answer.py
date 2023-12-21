
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[6]
    left_truncatable_primes = []
    
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        elif all(isprime(int(str_num[i:])) for i in range(len(str_num))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
