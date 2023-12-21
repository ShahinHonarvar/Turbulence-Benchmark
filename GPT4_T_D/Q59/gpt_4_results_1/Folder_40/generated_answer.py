
from itertools import permutations
import sympy

def all_left_truncatable_prime(tuple_of_pos):
    x = tuple_of_pos[10]
    prime_lst = [str(i) for i in sympy.primerange(0, x) if '0' not in str(i)]
    truncatable_primes = []

    for prime in prime_lst:
        for j in range(len(prime)):
            if sympy.isprime(int(prime[j:])):
                continue
            else:
                break
        else:
            truncatable_primes.append(int(prime))

    return sorted(truncatable_primes, reverse=True)
