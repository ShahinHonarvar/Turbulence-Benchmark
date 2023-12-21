
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_left_truncatable_prime = True
        truncated_num = str(num)
        while len(truncated_num) > 0:
            if not is_prime(int(truncated_num)):
                is_left_truncatable_prime = False
                break
            truncated_num = truncated_num[1:]
        if is_left_truncatable_prime:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
