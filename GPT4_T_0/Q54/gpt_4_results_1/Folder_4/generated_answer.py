
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[96]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                break
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
