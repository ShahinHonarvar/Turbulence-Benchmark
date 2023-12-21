
from sympy import isprime

def all_right_truncatable_prime(tuple):
    x = tuple[758]
    right_truncatable_primes = []
    for i in range(2, x):
        str_i = str(i)
        if all(isprime(int(str_i[j:])) for j in range(len(str_i))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
