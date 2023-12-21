
from itertools import permutations
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[73]
    right_truncatable_primes = []
    for i in range(2, x):
        numbers = list(str(i))
        perms = [''.join(p) for p in permutations(numbers)]
        if all(isprime(int(num)) for num in perms):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
