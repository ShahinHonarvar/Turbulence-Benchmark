
def all_right_truncatable_prime(tup):
    from sympy import isprime
    
    def truncate(n):
        return int(str(n)[:-1])

    def is_right_truncatable_prime(n):
        while n:
            if not isprime(n):
                return False
            n = truncate(n)
        return True
    
    x = tup[767]
    return sorted([p for p in range(x) if is_right_truncatable_prime(p)], reverse=True)
