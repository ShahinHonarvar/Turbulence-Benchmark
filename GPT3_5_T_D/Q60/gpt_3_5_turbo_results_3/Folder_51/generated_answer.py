
from math import isqrt
from itertools import combinations

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    valid_primes = []
    for i in range(2, x + 1):
        if "0" in str(i):
            continue
        if is_prime(i):
            num_str = str(i)
            for j in range(1, len(num_str)):
                left_num = int(num_str[j:])
                right_num = int(num_str[:-j])
                if not (is_prime(left_num) and is_prime(right_num)):
                    break
            else:
                valid_primes.append(i)
    return sorted(valid_primes)
