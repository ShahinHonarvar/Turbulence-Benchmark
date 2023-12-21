
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[177]
    truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable_prime = True
        for i in range(len(num_str)):
            left_part = int(num_str[i:])
            right_part = int(num_str[:i+1])
            if not is_prime(left_part) or not is_prime(right_part):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
