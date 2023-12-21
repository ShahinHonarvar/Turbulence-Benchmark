
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            digits = str(num)
            is_truncatable_prime = True
            for i in range(1, len(digits)):
                left_truncated = int(''.join(digits[i:]))
                right_truncated = int(''.join(digits[:-i]))
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                primes.append(num)
    return sorted(primes, reverse=True)
