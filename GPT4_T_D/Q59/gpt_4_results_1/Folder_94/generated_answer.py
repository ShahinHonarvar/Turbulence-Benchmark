
from sympy import isprime

def all_left_truncatable_prime(nums):
    def check_left_truncate(p):
        str_p = str(p)
        for i in range(len(str_p)):
            if not isprime(int(str_p[i:])):
                return False
        return True

    x = nums[43]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            if check_left_truncate(num):
                result.append(num)
    return sorted(result)
