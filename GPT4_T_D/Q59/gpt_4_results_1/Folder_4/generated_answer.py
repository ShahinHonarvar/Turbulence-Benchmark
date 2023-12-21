
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    all_primes = []

    for number in range(2, x):
        str_number = str(number)
        if '0' in str_number:
            continue
        if all(isprime(int(str_number[i:])) for i in range(len(str_number))):
            all_primes.append(number)

    all_primes.sort(reverse=True)
    return all_primes
