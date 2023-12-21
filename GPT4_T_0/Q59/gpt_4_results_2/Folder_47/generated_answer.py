
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[49]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if isprime(num):
            temp = str(num)
            while len(temp) > 0:
                if not isprime(int(temp)):
                    break
                temp = temp[1:]
            else:
                primes.append(num)
    return sorted(primes)
