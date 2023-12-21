
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[14]

    def left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    primes = []
    for i in range(10, x):
        if '0' not in str(i) and left_truncatable(i):
            primes.append(i)
            
    return sorted(primes, reverse=True)
