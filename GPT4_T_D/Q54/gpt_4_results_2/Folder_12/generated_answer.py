
def all_right_truncatable_prime(t):
    import sympy as sp
    def is_right_truncatable(n):
        for i in range(len(str(n)) - 1):
            n //= 10
            if not sp.isprime(n):
                return False
        return True

    x = t[70]
    result = [i for i in range(x) if sp.isprime(i) and is_right_truncatable(i)]
    return sorted(result, reverse=True)
