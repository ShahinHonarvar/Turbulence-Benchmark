
import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num) and all(sympy.isprime(int(str(num)[i:])) for i in range(len(str(num)))): # Checking for left-truncatable prime
            truncatable_primes.append(num)
    return truncatable_primes
