
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[86]
    # All possible numbers less than x
    nums = [str(n) for n in range(2, x)]
    # Get right-truncatable prime numbers
    trunc_primes = [int(num) for num in nums if is_right_truncatable_prime(num)]
    # Sort the numbers in descending order
    trunc_primes.sort(reverse=True)
    return trunc_primes

def is_right_truncatable_prime(num):
    while num:
        if not isprime(int(num)):
            return False
        num = num[:-1]
    return True
