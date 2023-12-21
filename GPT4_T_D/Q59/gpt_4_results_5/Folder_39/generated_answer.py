
import sympy

def all_left_truncatable_prime(nums):
    def is_prime(n):
        return sympy.isprime(n)

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    lt_primes = [i for i in range(nums[30]) if is_prime(i) and is_left_truncatable_prime(i)]
    return sorted(lt_primes, reverse=True)
