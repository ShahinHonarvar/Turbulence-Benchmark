import re
import sys
def all_right_truncatable_prime(n):
    for num in range(2, int(str(n)[-1]) + 1):
        if is_right_truncatable_prime(num):
            yield num
    return
def is_right_truncatable_prime(num):
    # If num is a prime number, it will remain prime when the last digit is
    # removed.
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13 or num == 17:
        return True
    # Check if num is a prime number.
    if num < 2 or num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        return False
    # If num is a prime number, it will remain prime when the last digit is
    # removed.
    return True
