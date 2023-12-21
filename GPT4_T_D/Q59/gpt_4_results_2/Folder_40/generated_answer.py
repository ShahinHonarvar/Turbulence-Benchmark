
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[10]
    primes = []
    for i in range(10, x):
        if '0' in str(i):
            continue
        lst = list(str(i))
        for p in range(1, len(lst)):
            if not is_prime(int(''.join(lst[p:]))):
                break
        else:
            if is_prime(i):
                primes.append(i)
    return sorted(primes, reverse=True)
