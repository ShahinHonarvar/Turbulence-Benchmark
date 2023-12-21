
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[6]
    right_truncatable_primes = []

    for i in range(2, x):
        num = str(i)
        for j in range(len(num)):
            if not isprime(int(num[j:])):
                break
        else:
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes, reverse=True)
