
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[803]
    def is_right_truncatable_prime(n):
        return all(isprime(int(str(n)[:-i])) for i in range(len(str(n))))

    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)
