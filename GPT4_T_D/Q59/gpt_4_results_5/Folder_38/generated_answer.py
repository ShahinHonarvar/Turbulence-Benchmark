
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[28]

    numbers = list(range(11, x))
    left_truncatable_primes = []
    
    for num in numbers:
        if '0' in str(num):
            continue
        if all(isprime(int(str(num)[i:])) for i in range(len(str(num)))):
            left_truncatable_primes.append(num)

    return sorted(left_truncatable_primes)
