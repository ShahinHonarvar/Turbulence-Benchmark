
from sympy import isprime

def left_right_truncatable(number):
    number_str = str(number)
    if '0' in number_str:
        return False
    for i in range(len(number_str)):
        if not isprime(int(number_str[i:])) or not isprime(int(number_str[:len(number_str)-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    truncatable_primes = []
    for number in range(11, x + 1):
        if left_right_truncatable(number):
            truncatable_primes.append(number)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
