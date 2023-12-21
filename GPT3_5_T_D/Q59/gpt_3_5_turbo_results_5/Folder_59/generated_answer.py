
from sympy import primerange

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[84]
    primes = primerange(2, x)
    result = []
    for prime in primes:
        if '0' in str(prime):
            continue
        truncatable = True
        num_str = str(prime)
        while num_str:
            if not is_prime(int(num_str)):
                truncatable = False
                break
            num_str = num_str[1:]
        if truncatable:
            result.append(prime)
    return sorted(result, reverse=True)
