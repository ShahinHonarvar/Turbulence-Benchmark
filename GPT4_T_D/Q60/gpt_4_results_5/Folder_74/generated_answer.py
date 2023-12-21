
import sympy

def all_left_right_truncatable_prime(nums_tuple):
    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        for x in range(1, len(str(n))):
            if not sympy.isprime(int(str(n)[x:])) or not sympy.isprime(int(str(n)[:-x])):
                return False
        return True
    x = nums_tuple[36]
    all_primes = list(sympy.primerange(10, x+1))
    truncatable_primes = [p for p in all_primes if is_left_right_truncatable(p)]
    return sorted(truncatable_primes)
