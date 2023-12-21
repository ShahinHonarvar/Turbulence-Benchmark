
from math import isqrt
from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for num in range(2, x + 1):
        if all(str(num).count(digit) == 1 for digit in '0245689'):
            truncated_num = num
            while is_prime(truncated_num):
                if truncated_num < 100:
                    primes.append(truncated_num)
                    break
                truncated_num = int(str(truncated_num)[:-1])
    return sorted(primes)
