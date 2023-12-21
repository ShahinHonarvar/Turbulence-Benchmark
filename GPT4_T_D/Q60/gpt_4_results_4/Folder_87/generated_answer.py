
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    primes = []
    for number in range(10, x+1):
        if isprime(number) and '0' not in str(number):
            truncated = [int(str(number)[i:-i] or str(number)[0]) for i in range(len(str(number)))]
            primes.append(number) if all(isprime(num) for num in truncated) else None
    return sorted(primes, reverse=True)
