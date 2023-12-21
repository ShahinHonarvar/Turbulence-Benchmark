
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    primes = []
    for num in range(2, x + 1):
        if not '0' in str(num):
            left_right_truncatable = True
            for i in range(1, len(str(num))):
                left_truncated = int(str(num)[i:])
                right_truncated = int(str(num)[:-i])
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
