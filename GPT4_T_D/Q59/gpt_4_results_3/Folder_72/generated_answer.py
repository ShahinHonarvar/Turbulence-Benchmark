
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[31]
    res = []

    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    for i in range(11, x):
        if is_left_truncatable(i):
            res.append(i)
    res.sort(reverse=True)
    return res
