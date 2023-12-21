
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[69]
    primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            temp = str(num)
            while len(temp) > 0 and isprime(int(temp)):
                temp = temp[1:]
            if len(temp) == 0:
                primes.append(num)
    return sorted(primes, reverse=True)
