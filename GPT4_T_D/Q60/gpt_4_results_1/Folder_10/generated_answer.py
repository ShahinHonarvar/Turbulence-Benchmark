
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[38]
    primes = []
    for n in range(11, x + 1):
        if '0' in str(n):
            continue
        flag = True
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:len(str(n))-i])):
                flag = False
        if flag:
            primes.append(n)
    return sorted(primes, reverse=True)
