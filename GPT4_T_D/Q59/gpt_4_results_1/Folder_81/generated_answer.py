
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[98]
    left_truncatable_primes = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        length = len(str(num))
        left_truncated_nums = [int(str(num)[i:]) for i in range(length)]
        if all(isprime(n) for n in left_truncated_nums):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes
