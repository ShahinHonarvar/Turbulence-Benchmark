
from math import isqrt
from typing import List

def all_left_truncatable_prime(numbers: tuple) -> List[int]:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[177]
    left_truncatable_primes = []
    
    for num in range(2, x):
        if '0' in str(num):
            continue

        truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                truncatable = False
                break

        if truncatable:
            left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes)
