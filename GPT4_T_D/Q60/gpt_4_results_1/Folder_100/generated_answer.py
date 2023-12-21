
from sympy import isprime

def generate_primes(n):
    primes = [2, 3, 5, 7]
    for p in primes:
        yield p
    num = 10
    while num <= n:
        if isprime(num) and all(isprime(int(str(num)[:i])) and isprime(int(str(num)[i:])) for i in range(1, len(str(num)))):
            yield num
        num += 1

def all_left_right_truncatable_prime(t):
    x = t[26]
    return sorted(list(generate_primes(x)))
