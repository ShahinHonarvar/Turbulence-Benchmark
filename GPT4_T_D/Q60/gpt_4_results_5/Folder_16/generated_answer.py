
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[792]
    primes = []
    digits = '123456789'
    for i in range(1, len(str(x))+1):
        for p in product(digits, repeat=i):
            num_str = ''.join(p)
            num = int(num_str)
            for j in range(len(num_str)):
                if num <= x and isprime(num):
                    num_str = num_str[1:-1]
                    num = int(num_str) if num_str else 0
                else:
                    break
            else:
                if num_str and num <= x and isprime(num):
                    primes.append(int(''.join(p)))

    return sorted(primes)
