
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        prime_check = all(isprime(int(str(num)[i:])) for i in range(len(str(num))))
        if prime_check:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
