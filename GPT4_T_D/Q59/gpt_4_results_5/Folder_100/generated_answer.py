
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[26]
    all_numbers = set(range(10, x))
    left_truncatable_primes = []

    for number in all_numbers:
        if '0' in str(number):
            continue
        num_str = str(number)
        num_len = len(num_str)
        if all(isprime(int(num_str[i:])) for i in range(num_len)):
            left_truncatable_primes.append(number)

    return sorted(left_truncatable_primes)
