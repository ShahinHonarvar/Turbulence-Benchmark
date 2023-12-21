
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[43]

    def is_left_truncatable_prime(n):
        if "0" in str(n):
            return False
        length = len(str(n))
        return all(isprime(int(str(n)[i:])) for i in range(length))

    prime_lst = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    prime_lst.sort()
        
    return prime_lst
