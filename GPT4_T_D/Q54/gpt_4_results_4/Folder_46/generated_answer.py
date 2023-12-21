
def all_right_truncatable_prime(t):
    from sympy import isprime
    
    def is_truncatable_prime(n):
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    
    x = t[33]
    result = [i for i in range(2, x) if is_truncatable_prime(i)]
    return sorted(result)
