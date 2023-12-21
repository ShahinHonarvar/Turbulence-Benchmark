
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[84]
    result = []
    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                is_truncatable = True
                for i in range(1, len(num_str)):
                    left_trunc = int(num_str[i:])
                    right_trunc = int(num_str[:len(num_str)-i])
                    if not is_prime(left_trunc) or not is_prime(right_trunc):
                        is_truncatable = False
                        break
                if is_truncatable:
                    result.append(num)
    return sorted(result, reverse=True)
