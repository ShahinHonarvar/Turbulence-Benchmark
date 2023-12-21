
import sympy

def all_right_truncatable_prime(nums):
    x = nums[11]
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not sympy.isprime(int(str_n[i:])):
                return False
        return True
    primes = [p for p in range(2, x-1) if sympy.isprime(p)]
    return sorted([p for p in primes if is_right_truncatable_prime(p)])
