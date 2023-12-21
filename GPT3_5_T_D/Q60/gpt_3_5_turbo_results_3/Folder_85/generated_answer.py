
from itertools import combinations


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and '0' not in str(num):
            digits = str(num)
            left_truncatable = True
            right_truncatable = True
            while digits != '':
                if not is_prime(int(digits)):
                    left_truncatable = False
                    break
                digits = digits[1:]
            digits = str(num)
            while digits != '':
                if not is_prime(int(digits)):
                    right_truncatable = False
                    break
                digits = digits[:-1]
            if left_truncatable and right_truncatable:
                primes.append(num)
    return sorted(primes)
