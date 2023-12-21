
from sympy import isprime

def all_right_truncatable_prime(tuple_of_integers):
    def right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = tuple_of_integers[992]
    right_truncatable_primes = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes)
