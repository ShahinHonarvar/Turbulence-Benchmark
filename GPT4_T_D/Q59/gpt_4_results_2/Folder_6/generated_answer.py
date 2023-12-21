
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    __left_truncatable_primes = []

    def is_left_prime(n):
        return isprime(n) and (n < 10 or (n//10 % 10 != 0 and is_left_prime(n // 10)))

    for i in range(11, x):
        if is_left_prime(i):
            __left_truncatable_primes.append(i)
    
    return sorted(__left_truncatable_primes)
