
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[77]
    left_truncatables = []

    def is_left_truncatable(n):
        str_n = str(n)
        if any (char == '0' for char in str_n):
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    for n in range(10, x):
        if is_left_truncatable(n):
            left_truncatables.append(n)
            
    return sorted(left_truncatables, reverse = True)
