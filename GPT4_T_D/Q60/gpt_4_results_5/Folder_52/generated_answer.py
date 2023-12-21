
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[52]
    primes = []
    for num in range(10, x+1):
        if '0' not in str(num) and isprime(num):
            for i in range(1, len(str(num))-1):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
