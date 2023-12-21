
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[49]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all(isprime(int(str_num[i:])) for i in range(len(str_num))):
            primes.append(num)
    return sorted(primes)
