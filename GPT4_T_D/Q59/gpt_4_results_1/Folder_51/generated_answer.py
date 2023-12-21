
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[54]
    left_truncatable_primes = []
    for num in range(11, x):
        num_str = str(num)
        if '0' not in num_str and isprime(num):
            is_truncatable_prime = True
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
