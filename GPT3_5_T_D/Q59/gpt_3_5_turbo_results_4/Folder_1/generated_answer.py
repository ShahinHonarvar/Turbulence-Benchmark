
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    primes = []
    for num in range(x - 1, 2, -1):
        if all(int(digit) in {1, 2, 3, 4, 5, 6, 7, 8, 9} for digit in str(num)):
            is_left_truncatable = True
            for i in range(len(str(num))):
                truncated_num = int(str(num)[i:])
                if not is_prime(truncated_num):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
