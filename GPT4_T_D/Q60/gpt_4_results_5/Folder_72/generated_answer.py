
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[31]
    
    def is_truncatable(n):
        str_n = str(n)
        for x in range(len(str_n)):
            if not isprime(int(str_n[x:])) or not isprime(int(str_n[:x+1])):
                return False
        return True

    truncatable_primes_lst = [p for p in range(10, x+1) if '0' not in str(p) and is_truncatable(p)]
    truncatable_primes_lst.sort(reverse=True)

    return truncatable_primes_lst
