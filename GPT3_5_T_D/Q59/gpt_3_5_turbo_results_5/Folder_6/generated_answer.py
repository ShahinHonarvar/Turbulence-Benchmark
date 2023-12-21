
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[74]

    truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(num)

    return sorted(truncatable_primes)
