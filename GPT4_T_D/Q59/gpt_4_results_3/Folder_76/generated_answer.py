
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[370]
    
    def check_num(num_str):
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True

    left_truncatable_primes = []
    for i in range(11, x):
        if '0' not in str(i) and isprime(i) and check_num(str(i)):
            left_truncatable_primes.append(i)

    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
