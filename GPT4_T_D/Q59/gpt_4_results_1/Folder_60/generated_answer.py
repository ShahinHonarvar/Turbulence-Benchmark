
import sympy

def left_truncatable_prime(prime):
    if '0' in str(prime):
        return False
    for i in range(1, len(str(prime))):
        if not sympy.isprime(int(str(prime)[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[87]
    return sorted([i for i in range(2, x) if sympy.isprime(i) and left_truncatable_prime(i)])
