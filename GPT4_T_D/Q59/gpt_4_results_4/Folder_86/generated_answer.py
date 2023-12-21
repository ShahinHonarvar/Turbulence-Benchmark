
from itertools import permutations
from sympy import isprime

def all_left_truncatable_prime(tple):
    x = tple[126]
    primes = [2, 3, 5, 7]
    for number_length in range(2, len(str(x))):
        new_primes = []
        for prime in primes:
            for next_digit in range(1, 10, 2):
                num_str = str(next_digit) + str(prime)
                if isprime(int(num_str)):
                    new_primes.append(int(num_str))
        primes = new_primes
    primes = [prime for prime in primes if prime < x]
    primes.sort(reverse=True)
    return primes
