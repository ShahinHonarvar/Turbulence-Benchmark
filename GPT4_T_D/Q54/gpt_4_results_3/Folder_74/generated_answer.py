
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[36]
    truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if all(isprime(int(str_num[:len(str_num)-i])) for i in range(len(str_num))):
            truncatable_primes.append(num)
    truncatable_primes.sort()
    return truncatable_primes
