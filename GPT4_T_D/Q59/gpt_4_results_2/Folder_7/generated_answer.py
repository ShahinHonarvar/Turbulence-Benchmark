
from sympy import isprime
from itertools import product

def all_left_truncatable_prime(t):
    x = t[803]
    lt_primes = []
    digits = '123456789'
    for length in range(1, len(str(x))):
        for s in product(digits, repeat=length):
            num_str = ''.join(s)
            num = int(num_str)
            if num > x:
                continue
            if all(isprime(int(num_str[i:])) for i in range(len(num_str))):
                lt_primes.append(num)
    return sorted(lt_primes)
