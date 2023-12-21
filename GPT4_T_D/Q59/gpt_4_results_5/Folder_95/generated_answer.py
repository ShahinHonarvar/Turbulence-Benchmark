
def all_left_truncatable_prime(tup):
    from sympy import isprime
    
    def check_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    
    x = tup[77]
    return sorted([i for i in range(2, x) if check_truncatable(i)])
