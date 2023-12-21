
from math import isqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[10]

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 2:
            if not is_prime(int(str_n[1:len(str_n)-1])):
                return False
            str_n = str_n[1:len(str_n)-1]
        return True

    results = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_truncatable_prime(num):
            results.append(num)

    return results
