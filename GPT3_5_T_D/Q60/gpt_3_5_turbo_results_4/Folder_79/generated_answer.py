
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[91]
    primes = []

    for i in range(2, x + 1):
        if is_prime(i):
            num_str = str(i)
            if '0' not in num_str:
                is_left_right_truncatable = True
                for j in range(1, len(num_str)):
                    left_truncated = int(num_str[j:])
                    right_truncated = int(num_str[:len(num_str) - j])
                    if not is_prime(left_truncated) or not is_prime(right_truncated):
                        is_left_right_truncatable = False
                        break
                if is_left_right_truncatable:
                    primes.append(i)

    return sorted(primes)
