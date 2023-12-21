
import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated_num = num
        while truncated_num > 10:
            truncated_num //= 10
            if not is_prime(truncated_num):
                break
        else:
            primes.append(num)
    return sorted(primes, reverse=True)
