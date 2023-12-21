
import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    primes = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        truncated = num
        is_left_truncatable_prime = True
        while truncated > 0:
            if not is_prime(truncated):
                is_left_truncatable_prime = False
                break
            truncated //= 10
        if is_left_truncatable_prime:
            primes.append(num)
    return sorted(primes, reverse=True)
