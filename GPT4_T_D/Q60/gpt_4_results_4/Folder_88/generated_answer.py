
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    if len(tup) <= 93:
        return []
    x = tup[93]
    prime = [str(n) for n in range(10, x + 1) if isprime(n)]
    n = 0
    while n < len(prime):
        num = prime[n]
        if '0' not in num and all(isprime(int(num[i:])) and isprime(int(num[:len(num) - i])) for i in range(1, len(num))):
            n += 1
        else:
            prime.remove(num)
    return sorted(map(int, prime))
