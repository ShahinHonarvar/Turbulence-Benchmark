
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[31]

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not (isprime(int(str_n[i:])) and isprime(int(str_n[:len(str_n)-i]))):
                return False
        return True

    truncatable_primes = []
    for i in range(13, x+1): 
        if is_left_right_truncatable(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
