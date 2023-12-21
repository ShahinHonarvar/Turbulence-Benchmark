
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[32]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            prime = True
            digits = str(i)
            while prime and len(digits) > 1:
                digits = digits[:-1]
                if not is_prime(int(digits)):
                    prime = False
            if prime:
                primes.append(i)
    return sorted(primes)
