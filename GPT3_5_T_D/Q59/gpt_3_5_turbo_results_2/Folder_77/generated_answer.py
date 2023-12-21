
import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(len(str(num))):
            truncated = str(num)[i:]
            if not is_prime(int(truncated)):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)
