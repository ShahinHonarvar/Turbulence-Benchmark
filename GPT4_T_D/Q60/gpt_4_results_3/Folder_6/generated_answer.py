
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[74]
    res = []
    
    def is_truncatable(p):
        str_p = str(p)
        p_len = len(str_p)
        if "0" in str_p:
            return False
        else:
            for i in range(p_len):
                if not (isprime(int(str_p[i:])) and isprime(int(str_p[:p_len-i]))):
                    return False
            return True

    for num in range(10, x + 1):
        if isprime(num) and is_truncatable(num):
            res.append(num)
            
    return sorted(res)
