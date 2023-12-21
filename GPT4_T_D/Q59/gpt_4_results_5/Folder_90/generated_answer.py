
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[466]
    primes_list = []
    
    def check_left_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
    
    for num in range(2, x):
        if "0" not in str(num):
            if isprime(num) and check_left_truncatable(num):
                primes_list.append(num)
                
    return sorted(primes_list, reverse=True)
