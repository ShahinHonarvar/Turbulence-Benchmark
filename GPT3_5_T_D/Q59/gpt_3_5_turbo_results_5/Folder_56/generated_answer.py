
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                is_left_truncatable = True
                for i in range(1, len(num_str)):
                    truncated_num = int(num_str[i:])
                    if not is_prime(truncated_num):
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    primes.append(num)
    return sorted(primes)
