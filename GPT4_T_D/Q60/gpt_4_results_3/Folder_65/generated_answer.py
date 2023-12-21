
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]
    truncatable_primes = []
    for num in range(10, x+1):
        num_str = str(num)
        if all(isprime(int(num_str[i:])) and isprime(int(num_str[:len(num_str) - i])) for i in range(len(num_str))):
            truncatable_primes.append(num)
    return truncatable_primes
