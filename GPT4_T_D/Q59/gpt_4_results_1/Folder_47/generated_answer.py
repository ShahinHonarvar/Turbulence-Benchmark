
import sympy

def all_left_truncatable_prime(t):
    def is_left_truncatable_prime(prime):
        s = str(prime)
        if '0' in s: return False
        return all(sympy.isprime(int(s[i:])) for i in range(len(s)))

    x = t[49]
    return sorted(i for i in range(2, x) if is_left_truncatable_prime(i))
