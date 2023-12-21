
from math import isqrt

def all_left_truncatable_prime(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, isqrt(number) + 1):
            if number % i == 0:
                return False
        return True

    def is_left_truncatable_prime(number):
        if '0' in str(number):
            return False
        for i in range(len(str(number))):
            if not is_prime(int(str(number)[i:])):
                return False
        return True

    x = numbers[26]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result
