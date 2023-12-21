
from sympy import isprime

def is_left_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    length = len(str_n)
    return all(isprime(int(str_n[i:])) for i in range(length))


def all_left_truncatable_prime(nums):
    try:
        x = nums[32]
    except IndexError:
        return "Insufficient length of tuple"
    return sorted(i for i in range(2, x) if is_left_truncatable_prime(i))
