
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        truncatable = True
        current_num = num
        while current_num > 10:
            if not is_prime(current_num):
                truncatable = False
                break
            str_num = str(current_num)
            current_num = int(str_num[1:-1])
        if truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)
