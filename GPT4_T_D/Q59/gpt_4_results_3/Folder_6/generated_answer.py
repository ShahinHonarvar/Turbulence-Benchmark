
from itertools import product
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[74]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    def generate_primes(n):
        return [int(''.join(map(str,numbers))) for numbers in product(range(10), repeat=n) if is_left_truncatable_prime(int(''.join(map(str,numbers))))]

    primes = []
    for i in range(1, len(str(x))):
        primes.extend(generate_primes(i))

    return sorted([prime for prime in primes if prime < x])
