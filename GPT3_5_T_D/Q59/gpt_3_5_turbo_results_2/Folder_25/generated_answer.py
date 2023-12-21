
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[92]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated_num = str(num)
        while truncated_num:
            if not is_prime(int(truncated_num)):
                break
            truncated_num = truncated_num[1:]
        else:
            primes.append(num)
    return primes
