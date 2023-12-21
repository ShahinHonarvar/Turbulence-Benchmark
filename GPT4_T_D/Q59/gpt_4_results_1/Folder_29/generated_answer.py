
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    primes = list(filter(isprime, range(2, x)))
    left_truncatable_primes = []
    
    for prime in primes:
        if '0' not in str(prime):
            temp = str(prime)
            while len(temp) > 0:
                if not isprime(int(temp)):
                    break
                temp = temp[1:]
            if len(temp) == 0:
                left_truncatable_primes.append(prime)

    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
