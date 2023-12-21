
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[28]
    right_truncatable_primes = []
    for num in range(2, x):
        right_truncatable = True
        for i in range(len(str(num))):
            if not isprime(int(str(num)[:len(str(num))-i])):
                right_truncatable = False
                break
        if right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
