import sys
import itertools
import bisect
def all_left_truncatable_prime(nums):
    result = []
    for prime in nums:
        is_left_truncatable = True
        while prime:
            prime //= 10
            if not prime:
                break
            elif not prime.is_prime():
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(prime)
    return result
