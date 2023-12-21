
from sympy import isprime

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[100]
    right_truncatable_primes = []
    for i in range(2, x):
        str_i = str(i)
        if all(isprime(int(str_i[:j])) for j in range(1, len(str_i) + 1)):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
