
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[54]
    truncatable_primes = []
    for i in range(10, x):
        num_str = str(i)
        if '0' in num_str:
            continue
        elif all(isprime(int(num_str[j:])) for j in range(len(num_str))):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
