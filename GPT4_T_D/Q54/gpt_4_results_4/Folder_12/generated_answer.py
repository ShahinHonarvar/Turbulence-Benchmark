
def all_right_truncatable_prime(tuple):
    import sympy

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not sympy.isprime(int(n[i:])):
                return False
        return True

    x = tuple[70]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    
    return sorted(result, reverse=True)
