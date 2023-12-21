
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[177]

    def is_right_truncatable_prime(num):
        num = str(num)
        while len(num) > 0:
            if not isprime(int(num)):
                return False
            num = num[:-1]
        return True
    
    prime_list = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            prime_list.append(i)
    
    return sorted(prime_list)
