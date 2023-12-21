
from sympy import isprime

def is_left_truncatable_prime(n):
    while n > 0:
        if not isprime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    truncatable_primes = []
    
    for num in range(x-1, 1, -1):
        if is_left_truncatable_prime(num):
            truncatable_primes.append(num)
    
    return truncatable_primes
