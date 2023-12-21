
def all_right_truncatable_prime(t):
    import sympy

    def check_truncatable(n):
        while n != 0:
            if not sympy.isprime(n):
                return False
            n = n // 10
        return True

    x = t[767]
    return sorted([i for i in range(2,x) if check_truncatable(i)], reverse=True)
