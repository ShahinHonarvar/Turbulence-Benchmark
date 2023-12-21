
def all_left_right_truncatable_prime(numbers):
    import sympy

    def is_truncatable_prime(p):
        if '0' in str(p): return False
        p = str(p)
        return all(sympy.isprime(int(p[i:len(p)-i])) for i in range(len(p)))

    x = numbers[98]
    return sorted(filter(is_truncatable_prime, sympy.primerange(10, x + 1)))
