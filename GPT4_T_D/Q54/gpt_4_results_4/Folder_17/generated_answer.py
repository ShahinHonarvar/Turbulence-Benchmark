
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[36]
    primes = []
    for num in range(2, x):
        is_right_truncatable_prime = True
        for j in range(len(str(num))):
            if not isprime(int(str(num)[:-j] or '0')):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            primes.append(num)
    return sorted(primes, reverse=True)
