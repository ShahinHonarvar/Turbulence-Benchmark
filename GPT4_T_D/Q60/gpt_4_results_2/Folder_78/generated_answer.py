
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[23]
    
    def is_lr_truncatable_prime(n):
        if '0' in str(n):
            return False

        length = len(str(n))
        for i in range(length):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:length-i])):
                return False
        return True

    return sorted(filter(is_lr_truncatable_prime, range(10, x+1)))
