
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[433]

    def truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:-i])):
                return False
        return True

    primes = [i for i in range(13, x + 1) if isprime(i) and truncatable_prime(i)]
    primes.sort(reverse=True)

    return primes
