
import sympy

def all_left_truncatable_prime(tup):
    num = tup[20]
    left_truncatable_primes = []
    
    def is_left_truncatable_prime(n):
        if not sympy.isprime(n):
            return False
        if n < 10:
            return True
        return is_left_truncatable_prime(int(str(n)[1:]))

    for n in range(2, num):
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)

    return sorted(left_truncatable_primes, reverse = True)
