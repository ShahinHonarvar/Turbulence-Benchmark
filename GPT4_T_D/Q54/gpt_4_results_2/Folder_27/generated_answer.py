
from itertools import permutations
from sympy import isprime

def all_right_truncatable_prime(nums):
    def is_right_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[:i])) for i in range(len(str_n), 0, -1))
    
    x = nums[79]
    right_truncatable_prime_lst = [n for n in range(2, x) if is_right_truncatable(n)]
    return sorted(right_truncatable_prime_lst, reverse=True)
