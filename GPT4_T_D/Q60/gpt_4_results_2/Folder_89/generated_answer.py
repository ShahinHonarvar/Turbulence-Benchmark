
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[97]
    truncatable_primes = []

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        length = len(str_num)
        for i in range(length):
            if not (isprime(int(str_num[i:])) and isprime(int(str_num[:(length-i)]))):
                return False
        return True
    
    for num in range(x+1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
            
    return sorted(truncatable_primes, reverse=True)
