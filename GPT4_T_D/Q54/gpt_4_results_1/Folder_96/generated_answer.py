
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[29]
    primes = []
    for num in range(2, x):
        num_str = str(num)
        if all(isprime(int(num_str[:i+1])) for i in range(len(num_str))):
            primes.append(num)
    return sorted(primes)
