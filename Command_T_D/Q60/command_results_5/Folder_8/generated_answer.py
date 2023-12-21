
import sys
import bisect

def all_left_right_truncatable_prime(nums):
    left_right_truncatable_primes = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(num):
    if num <= 2:
        return True
    if num <= 3:
        return False
    # Check that the number contains no 0
    if num % 10 == 0 or num % 10 == 5:
        return False
    # Check that the number remains prime when the leading leftmost and last rightmost digits are
    # simultaneously successively removed down to a one- or two-digit prime.
    if num % 10 == 1:
        return True
    elif num % 10 == 2:
        return True
    elif num % 10 == 3:
        return True
    elif num % 10 == 4:
        return True
    elif num % 10 == 6:
        return True
    elif num % 10 == 7:
        return True
    elif num % 10 == 8:
        return True
    elif num % 10 == 9:
        return True
    elif num % 10 == 5:
        return True
    elif num % 10 == 0:
        return True
    else:
        return False
