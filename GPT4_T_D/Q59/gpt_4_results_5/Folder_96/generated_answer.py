
from sympy import isprime

def all_left_truncatable_prime(tuple):
    x = tuple[29]
    all_left_truncatable_primes = []
    for number in range(2, x):
        string_number = str(number)
        if '0' in string_number:
            continue
        for i in range(len(string_number)):
            if not isprime(int(string_number[i:])):
                break
        else:
            all_left_truncatable_primes.append(number)
    all_left_truncatable_primes.sort()
    return all_left_truncatable_primes
