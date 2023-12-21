
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[22]

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if (not isprime(int(str_n[i:]))) or (not isprime(int(str_n[:len(str_n) - i]))):
                return False
        return True

    res = []
    for num in range(10, x+1):
        if '0' not in str(num) and is_truncatable(num):
            res.append(num)

    return sorted(res, reverse=True)
