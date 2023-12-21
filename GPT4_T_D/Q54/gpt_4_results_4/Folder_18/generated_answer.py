
from sympy import isprime

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[429]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                break
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
