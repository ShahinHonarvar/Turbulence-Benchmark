
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[92]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            n = str(i)
            is_truncatable_prime = True
            for j in range(len(n)):
                if not isprime(int(n[j:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(i)
    return truncatable_primes
