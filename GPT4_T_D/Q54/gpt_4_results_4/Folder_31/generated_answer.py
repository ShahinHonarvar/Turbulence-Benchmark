
from sympy import isprime

def all_right_truncatable_prime(nums):
    def is_right_truncatable_prime(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not isprime(int(str_num[0:i+1])):
                return False
        return True

    x = nums[50]
    results = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            results.append(i)

    results.sort(reverse=True)
    return results
