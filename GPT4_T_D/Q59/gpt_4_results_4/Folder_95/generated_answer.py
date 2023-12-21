
from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[77]
    all_primes = []
    for i in range(2, x):
        if all(isprime(int(str(i)[j:])) for j in range(len(str(i)))) and '0' not in str(i):
            all_primes.append(i)
    all_primes.sort()
    return all_primes
