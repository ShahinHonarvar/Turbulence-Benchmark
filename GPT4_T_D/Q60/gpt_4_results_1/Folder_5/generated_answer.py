
from itertools import combinations
from sympy import isprime

def all_left_right_truncatable_prime(num_tuple):
    num = num_tuple[55]
    trunc_primes = []
    
    for combo in combinations('123456789', num):
        perm = [''.join(combo[i: j]) for i in range(len(combo)) for j in range(i + 1, len(combo) + 1) if isprime(int(''.join(combo[i: j])))]
        if all(isprime(int(i)) for i in perm) and len(perm) > 1:
            trunc_primes.append(int(''.join(combo)))
    
    return sorted([i for i in trunc_primes if i <= num])
