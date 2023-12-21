
from sympy import isprime

def find_primes_between_indices(integer_list):
    primes = []
    for i in range(289, 382):
        try:
            if isprime(integer_list[i]):
                primes.append(integer_list[i])
        except IndexError:
            break
    return sorted(primes, reverse=True)
