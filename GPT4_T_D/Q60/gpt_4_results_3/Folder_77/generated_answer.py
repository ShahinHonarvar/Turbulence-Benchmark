
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[767]
    result = []
    
    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n)-i])):
                return False
        return True

    for i in range(13, x + 1, 2): 
        if is_left_right_truncatable_prime(i):
            result.append(i)

    return sorted(result, reverse=True)
