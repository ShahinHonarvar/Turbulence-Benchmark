
from math import isqrt

def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[7]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            if "0" not in str_num:
                truncatable = True
                for i in range(1, len(str_num)):
                    if not is_prime(int(str_num[i:])):
                        truncatable = False
                        break
                if truncatable:
                    primes.append(num)
    return sorted(primes)
