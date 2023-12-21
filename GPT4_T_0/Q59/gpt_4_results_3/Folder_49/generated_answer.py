
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[14]
    primes = []
    for num in range(2, x):
        if isprime(num):
            str_num = str(num)
            if '0' not in str_num:
                for i in range(len(str_num)):
                    if not isprime(int(str_num[i:])):
                        break
                else:
                    primes.append(num)
    return sorted(primes)
