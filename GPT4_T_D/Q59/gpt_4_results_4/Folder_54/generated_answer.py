
from sympy import isprime

def all_left_truncatable_prime(t):
    
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    x = t[88]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)
