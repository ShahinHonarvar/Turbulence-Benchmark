
def all_right_truncatable_prime(t):
    from sympy import isprime
    
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(isprime(int(str_n[:i])) for i in range(1, len(str_n) + 1))
    
    x = t[992]
    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)])
