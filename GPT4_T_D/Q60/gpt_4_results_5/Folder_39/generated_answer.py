
import sympy

def is_truncatable(p):
    if '0' in str(p):
        return False
    n = len(str(p))
    for i in range(1, n):
        left = int(str(p)[i:])
        right = int(str(p)[:-i])
        if not (sympy.isprime(left) and sympy.isprime(right)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[30]
    prime_list = [p for p in sympy.primerange(10, x + 1) if is_truncatable(p)]
    return sorted(prime_list, reverse=True)
