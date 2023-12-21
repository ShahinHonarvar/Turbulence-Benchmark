
import sympy

def all_left_truncatable_prime(nums):
    left_truncatable_primes = []
    for number in range(2, nums[24]):
        if not '0' in str(number) and sympy.isprime(number):
            is_left_truncatable = True
            for i in range(1,len(str(number))):
                if not sympy.isprime(int(str(number)[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes)
