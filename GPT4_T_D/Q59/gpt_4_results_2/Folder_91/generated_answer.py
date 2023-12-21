
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[0]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        num_str = str(num)
        primes = [isprime(int(num_str[i:])) for i in range(len(num_str))]
        if all(primes):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
