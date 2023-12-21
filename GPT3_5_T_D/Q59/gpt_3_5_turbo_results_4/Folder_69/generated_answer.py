
from typing import List
from math import isqrt

def all_left_truncatable_prime(nums: tuple) -> List[int]:
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

    x = nums[760]
    results = []

    for num in range(10, x):
        if '0' in str(num):
            continue
        if is_prime(num):
            truncate_num = str(num)
            is_truncatable_prime = True
            while len(truncate_num) > 1:
                truncate_num = truncate_num[1:]
                if not is_prime(int(truncate_num)):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                results.append(num)

    return sorted(results, reverse=True)
