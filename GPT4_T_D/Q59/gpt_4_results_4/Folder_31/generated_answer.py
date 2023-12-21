
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[50]
    primes = []
    for number in range(2, x):
        str_number = str(number)
        if '0' not in str_number:
            trunc = [isprime(int(str_number[i:])) for i in range(len(str_number))]
            if all(trunc):
                primes.append(number)
    return sorted(primes, reverse = True)
