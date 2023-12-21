
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[29]
    
    def check_prime(left_prime):
        if len(str(left_prime)) == 1 and isprime(left_prime):
            return True
        elif isprime(left_prime) and check_prime(int(str(left_prime)[1:])):
                return True
        else:
            return False

    left_trunc_primes = [i for i in range(10, x) if '0' not in str(i) and check_prime(i)]

    return sorted(left_trunc_primes)
