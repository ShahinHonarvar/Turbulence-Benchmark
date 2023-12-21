
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[28]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            truncate_check = True
            while truncate_check and len(str_num) > 1:
                str_num = str_num[:-1]
                if not is_prime(int(str_num)):
                    truncate_check = False
            if truncate_check:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
