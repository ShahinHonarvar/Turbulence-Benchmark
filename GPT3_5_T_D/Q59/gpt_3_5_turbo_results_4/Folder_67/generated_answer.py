
from sympy import isprime

def is_left_truncatable_prime(n):
    num = str(n)
    while len(num) > 1:
        num = num[1:]
        if not isprime(int(num)):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[71]
    primes = []
    for i in range(2, x):
        if isprime(i) and '0' not in str(i):
            if is_left_truncatable_prime(i):
                primes.append(i)
    primes.sort(reverse=True)
    return primes
