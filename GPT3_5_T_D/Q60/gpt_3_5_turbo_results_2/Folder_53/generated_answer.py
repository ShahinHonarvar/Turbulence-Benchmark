
from math import sqrt

def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable(num):
        if num < 10:
            return is_prime(num)
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:i+1])) or not is_prime(int(num_str[i:])):
                return False
        return True

    x = numbers[86]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
