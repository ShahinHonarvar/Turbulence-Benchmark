
def all_right_truncatable_prime(t):
    import sympy
    x = t[835]
    def check_truncatable(p):
        while p > 0:
            if not sympy.isprime(p):
                return False
            p //= 10
        return True
    truncatables = []
    for i in range(2, x):
        if check_truncatable(i):
            truncatables.append(i)
    return sorted(truncatables)
