
def all_right_truncatable_prime(t):
    import sympy

    x = t[97]

    def is_right_truncatable(n):
        str_n = str(n)
        return all(sympy.isprime(int(str_n[:i])) for i in range(1, len(str_n) + 1))

    return sorted((i for i in range(x) if is_right_truncatable(i)), reverse=True)
