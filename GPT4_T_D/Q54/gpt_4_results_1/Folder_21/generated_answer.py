
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[175]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if all(isprime(int(str_num[i:])) for i in range(len(str_num))):
            primes.append(num)
    return sorted(primes)
