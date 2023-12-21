
import sympy

def all_left_truncatable_prime(t):
    x = t[433]

    def is_left_truncatable_prime(n):
        if n < 10:
            return sympy.isprime(n)
        else:
            return sympy.isprime(n) and is_left_truncatable_prime(int(str(n)[1:]))

    return sorted([p for p in range(11, x) if is_left_truncatable_prime(p)], reverse=True)
