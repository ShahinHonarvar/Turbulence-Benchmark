
from math import sqrt
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def left_truncatable(n):
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[86]
    result = []
    for i in range(x):
        if '0' not in str(i) and is_prime(i) and left_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
