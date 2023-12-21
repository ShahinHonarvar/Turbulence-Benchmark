
import sympy

def all_left_truncatable_prime(nums):
    x = nums[1]
    primes = []
    for num in range(x-1, 1, -1):
        if sympy.isprime(num) and '0' not in str(num):
            truncatable = True
            for i in range(len(str(num))):
                if not sympy.isprime(int(str(num)[i:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
