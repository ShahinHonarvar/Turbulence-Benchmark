
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    def is_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not isprime(int(n[i:])) or not isprime(int(n[:len(n)-i])):
                return False
        return True

    x = nums[74]
    res = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            res.append(i)

    return sorted(res)
