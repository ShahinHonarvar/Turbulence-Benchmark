
import sympy

def all_left_right_truncatable_prime(nums):
    x = nums[88]
    all_primes = list(filter(sympy.isprime, range(1, x+1)))
    trunc_primes = []
    for prime in all_primes:
        if '0' in str(prime):
            continue
        truncatable = True
        for i in range(1, len(str(prime))):
            if not sympy.isprime(int(str(prime)[i:])) or not sympy.isprime(int(str(prime)[:-i])):
                truncatable = False
                break
        if truncatable:
            trunc_primes.append(prime)
    return sorted(trunc_primes, reverse=True)
