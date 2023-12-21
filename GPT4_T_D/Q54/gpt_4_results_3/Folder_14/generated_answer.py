
from sympy import isprime

def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[78]
    truncatable_primes = []

    for i in range(2, x):
        number = str(i)
        while len(number) > 0:
            if isprime(int(number)):
                number = number[:-1]
            else:
                break
        else:
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
