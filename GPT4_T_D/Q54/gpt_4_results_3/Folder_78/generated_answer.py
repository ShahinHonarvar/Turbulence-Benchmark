
def all_right_truncatable_prime(tup):
    import sympy
    x = tup[23]

    def is_right_truncatable_prime(n):
        if not sympy.isprime(n):
            return False
        while n > 10:
            n //= 10
            if not sympy.isprime(n):
                return False
        return True

    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)])
