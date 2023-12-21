
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[645]
    primes = []
    for i in range(2, x):
        if isprime(i) and '0' not in str(i):
            truncatable = True
            for j in range(1, len(str(i))):
                if not isprime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)
