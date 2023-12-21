
def all_right_truncatable_prime(t):
    from sympy import isprime

    def right_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[:len(str_n) - i])) for i in range(len(str_n)))
    
    x = t[433]

    return sorted([i for i in range(2, x) if right_truncatable(i)], reverse=True)
