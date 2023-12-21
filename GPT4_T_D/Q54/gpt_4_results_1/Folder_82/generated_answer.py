
from sympy import isprime

def all_right_truncatable_prime(tpl):
    def is_right_truncatable(n):
        for i in range(len(str(n))):
            if not isprime(n):
                return False
            n = n // 10
        return True
    
    x = tpl[69]
    return sorted([i for i in range(x) if is_right_truncatable(i)], reverse=True)
