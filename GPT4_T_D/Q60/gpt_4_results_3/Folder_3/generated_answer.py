
from itertools import product
from math import sqrt

def all_left_right_truncatable_prime(nums):
    x = nums[100]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all(is_prime(int(str_n[i:])) and is_prime(int(str_n[:len(str_n)-i])) for i in range(len(str_n)))

    return sorted(n for n in range(2, x+1) if is_truncatable_prime(n))
