
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[758]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            if '0' in num:
                continue
            is_left_truncatable = True
            for j in range(1, len(num)):
                if not is_prime(int(num[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return left_truncatable_primes
