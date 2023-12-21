
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[18]
    truncatable_primes = []
    for number in range(11, x + 1):
        if '0' in str(number):
            continue
        length = len(str(number))
        left_right_truncatable = True
        for i in range(length):
            if not isprime(int(str(number)[i:])) or not isprime(int(str(number)[:length - i])):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse = True)
