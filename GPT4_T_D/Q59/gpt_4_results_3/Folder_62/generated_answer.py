
from sympy import isprime

def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[70]
    eligible_numbers = [str(i) for i in range(1, x) if '0' not in str(i) and isprime(i)]
    left_truncatable_primes = []

    for number in eligible_numbers:
        for i in range(1, len(number)):
            if not isprime(int(number[i:])):
                break
        else:
            left_truncatable_primes.append(int(number))

    return sorted(left_truncatable_primes)
