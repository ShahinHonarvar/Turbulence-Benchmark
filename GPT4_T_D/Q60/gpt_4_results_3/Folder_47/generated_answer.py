
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    def is_left_right_truncatable(n):
        n = str(n)
        if '0' in n: return False
        size = len(n)
        for x in range(size):
            if not (isprime(int(n[x:])) and isprime(int(n[:size-x]))):
                return False
        return True

    result = []
    for x in range(10, nums[49]+1):
        if is_left_right_truncatable(x):
            result.append(x)
    return sorted(result)
