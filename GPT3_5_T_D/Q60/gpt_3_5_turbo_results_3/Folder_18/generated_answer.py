
from math import isqrt


def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if s[i] == '0':
                return False
            if not is_prime(int(s[i:])):
                return False
            if not is_prime(int(s[:i+1])):
                return False
        return True

    x = numbers[429]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)

    result.sort(reverse=True)
    return result
