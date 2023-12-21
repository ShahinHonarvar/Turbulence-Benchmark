
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[67]
    truncatable_primes = []

    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        is_truncatable_prime = True
        left_truncations = [int(str(num)[i:]) for i in range(len(str(num)))]
        right_truncations = [int(str(num)[:i]) for i in range(1, len(str(num)) + 1)]
        truncations = left_truncations + right_truncations
        for truncation in truncations:
            if not is_prime(truncation):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
