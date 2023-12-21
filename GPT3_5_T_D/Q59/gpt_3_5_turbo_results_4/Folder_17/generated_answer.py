
from sympy import isprime

def left_truncatable(number):
    num_str = str(number)
    while num_str:
        if not isprime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for num in range(x-1, 0, -1):
        if '0' not in str(num) and left_truncatable(num):
            primes.append(num)
    return primes
