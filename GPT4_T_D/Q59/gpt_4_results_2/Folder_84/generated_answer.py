
from sympy import isprime

def all_left_truncatable_prime(integers):
    x = integers[630]
    primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all(isprime(int(num_str[i:])) for i in range(len(num_str))):
            primes.append(num)
    primes.sort(reverse=True)
    return primes
