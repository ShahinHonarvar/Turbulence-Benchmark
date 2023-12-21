
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[69]
    
    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:-i])) for i in range(len(s)))
    
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True)
