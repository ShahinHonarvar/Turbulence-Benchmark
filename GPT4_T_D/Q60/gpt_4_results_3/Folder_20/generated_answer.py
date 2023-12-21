
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[100]
    
    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True

    return sorted([num for num in range(11, x+1) if is_left_right_truncatable(num)], reverse=True)
