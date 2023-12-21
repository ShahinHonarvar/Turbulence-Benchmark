
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[70]
    all_primes = []
    for num in range(2, x):
        if isprime(num):
            str_num = str(num)
            for i in range(len(str_num)):
                if not isprime(int(str_num[:-i])):
                    break
            else:
                all_primes.append(num)
    return sorted(all_primes, reverse=True)
