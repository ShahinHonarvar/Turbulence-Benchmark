
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[6]
    all_primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []

    def check_if_left_truncatable(num):
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    for prime in all_primes:
        if check_if_left_truncatable(prime) and '0' not in str(prime):
            left_truncatable_primes.append(prime)

    return sorted(left_truncatable_primes, reverse=True)
